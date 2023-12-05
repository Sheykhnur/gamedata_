# S.T.A.L.K.E.R. LTX config prettyfier  / Сортировщик LTX файлов
# 				by phobos2077
#
# requires python 3.x

from collections import OrderedDict
import configparser, os, re, pprint, argparse, glob
import ltx_defn 

pp = pprint.PrettyPrinter(indent=4)

# Parses given LTX file into a list of sections which are simple dictionaries with lists of lines inside
def parse(f):
	RE_INCLUDE = r'^\#include\s*"(?P<name>[^"]+)"'
	RE_SECTION = r'^\[(?P<name>.*)\](?P<inherit>:(\w+,)*\w+,?)?'
	RE_PAIR = r'^(?P<commented>\s*\;+)?\s*(?P<key>[$\w][$\w\-]*)\s*=\s*(?P<value>[^\;\n]*)?(?P<comment>[^\n]*)?$'
	RE_PAIR_NO_KEY = r'^\s*(?P<value>[^\;\n]+)(?P<comment>[^\n]*)?$'

	data = list()
	section = None
	prev_lines = list()

	for line in f:
		match = re.match(RE_SECTION, line) or re.match(RE_INCLUDE, line)
		if match:
			isInclude = (line[0] == '#')
			section = dict(
				name = match.group('name'),
				inherit = match.group('inherit')[1:].split(',') if not isInclude and match.group('inherit') else list(),
				line = line,
				pairs = list(),
				prev_lines = prev_lines,
				include = isInclude,
			)
			data.append(section)
			prev_lines = list()
		else:
			match = re.match(RE_PAIR, line)
			if match and section:
				pair = dict(
					line = line,
					key = match.group('key') if match else '',
					value = match.group('value') if match else '',
					comment = match.group('comment') if match else '',
					commented = bool(match.group('commented')),
					prev_lines = prev_lines,
				)
				section['pairs'].append(pair)
				prev_lines = list()
			else:
				match = re.match(RE_PAIR_NO_KEY, line)
				if match and section:
					pair = dict(
						line = line,
						value = match.group('value') if match else '',
						comment = match.group('comment') if match else '',
						prev_lines = prev_lines,
					)
					section['pairs'].append(pair)
					prev_lines = list()
				else:
					prev_lines.append(line)
	return data

# Takes parsed LTX file and for each section:
# - removes all comments between lines
# - detects type of section, like weapon, ammo, etc.
# - sorts all lines into groups according to detected type (or just alphabetically sorts if type unknown)
# - removes some lines according to type definition
def sort(ltx, allDefinitions):
	# first real section
	isFirstSection = True

	# First #include line in a block of includes
	isFirstInclude = True

	for sect in ltx:
		# Remove empty lines
		sect['prev_lines'] = [l for l in sect['prev_lines'] if l.strip()]
		if sect['include']:
			if isFirstInclude and not isFirstSection:
				sect['prev_lines'].insert(0, '\n\n')
				isFirstInclude = False
		else:
			isFirstInclude = True
			if isFirstSection:
				isFirstSection = False
			else:
				sect['prev_lines'].insert(0, '\n\n')

		fSort = lambda x: x['key'].lower()
		defnForSect = None
		for defn in allDefinitions:
			if defn['selector'](sect):
				defnForSect = defn
				break

		if defnForSect:
			availablePairs = [pair for pair in sect['pairs'] if not pair['key'] in defnForSect['deleteKeys']]
			sortedPairs = list()

			for (name, keys) in defnForSect['groups']:
				isFirstKey = True
				for keyre in keys:
					matchingKeys = sorted([pair for pair in availablePairs if re.match(keyre + '$', pair['key'])], key = fSort)
					for pair in matchingKeys:
						pair['prev_lines'] = ['\n; ' + name + '\n'] if isFirstKey else []
						sortedPairs.append(pair)
						availablePairs.remove(pair)
						isFirstKey = False

			for pair in availablePairs:
				pair['prev_lines'] = []

			# Prepend non-grouped lines
			sortedPairs = sorted(availablePairs, key = fSort) + sortedPairs
		else:
			sortedPairs = sorted(sect['pairs'], key = fSort)
			for pair in sortedPairs:
				pair['prev_lines'] = []

		sect['pairs'] = sortedPairs

# Takes parsed LTX and writes it back to a file
# - Empty lines will be skipped
# - All key/value pairs will be reindented according to indentLen
def writeLtx(fileName, sections, indentLen):
	f = open(fileName, 'w+')

	for sect in sections:

		for pline in sect['prev_lines']:
			f.write(pline)

		f.write(sect['line'])
		for pair in sect['pairs']:
			line = pair['line']
			prev_lines = pair['prev_lines']
			key = pair['key'] if 'key' in pair else None
			val = pair['value']
			comment = pair['comment']
			commented = '; ' if 'commented' in pair and pair['commented'] else ''
			for pline in prev_lines:
				f.write(pline)
			if key:
				f.write(commented + key + (' ' * (indentLen - len(key))) + '= ' + val + comment + '\n')
			else:
				f.write(val + comment + '\n')
	f.close()


argParser = argparse.ArgumentParser(description='Prettify LTX file configs by sorting keys in specific way, removing useless lines and indenting all lines.\n\n'+
	"[RU] Преображает LTX файлы конфигов путем пересортировки строк в удобном порядке, удаления лишних строк и задания одинаковых отступов.",
	formatter_class= argparse.RawTextHelpFormatter
	)

argParser.add_argument('input', type=str,
				   help='input LTX file/mask | имя входного файла (или маска)')
argParser.add_argument('-o', dest='outputDir', type=str, default="_pretty\\",
				   help='output dir name (by default "_pretty") | путь для записи выходных файлов')
argParser.add_argument('-i', dest='indentLen', type=int, default=40,
				   help='indentation length (default is 40) | линия выравнивания отступов (по умолчанию 40)')
argParser.add_argument('--no-sort', dest='noSort', action='store_const', const=True, default=False,
				   help='do not sort, only fix indent | только выровнять отступы, не сортировать')

args = argParser.parse_args()

# Safety check #1, don't rewrite source file!
if args.outputDir.strip() in ['', '.']:
	raise ValueError("Output cannot be current dir")

for fname in glob.glob(args.input):
	outputPath = args.outputDir + "\\" + fname

	# Safety check #2
	if os.path.abspath(fname) == os.path.abspath(outputPath):
		raise ValueError("Output cannot match input: " + fname)

	print('Parsing ' + fname + '...')
	
	fileHandle = open(fname)
	ltx = parse(fileHandle)
	
	if not args.noSort:
		print('Sorting...')
		sort(ltx, ltx_defn.allDefinitions)

	print('Writing output...')
	
	outputDir = os.path.dirname(outputPath)

	if not os.path.exists(outputDir):
	    os.makedirs(outputDir)

	writeLtx(outputPath, ltx, args.indentLen)

	# Safety #3: close input file after output, so it cannot be overwritten
	fileHandle.close()

print('Done!\n')
