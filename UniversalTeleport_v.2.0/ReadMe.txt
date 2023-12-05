====================================================
Название:	Universal Teleport v 2.0
Платформа:	S.T.A.L.K.E.R. Тень Чернобыля 1.0004
Автор:		naxac
====================================================
Мод добавляет в игру ручной телепортатор, с помощью которого можно переместиться в любую точку Зоны. Это дарит игроку полную свободу перемещения, незавсимо от сюжетной линии. Использовать прибор можно неограниченное количество раз, но для его использования необходимо иметь при себе любой артефакт. После использования (перемещения) артефакт преврщается в "булыжник" - тоже арт, но дешевый и без всяких свойств.
Прибор появляется в инвентаре в самом начале игры.
С помощью меню "Телепортация по координатам" можно переместиться в любую точку в пределах локации, на которой в данный момент находится ГГ. Инструкция - как это сделать - в том же меню.
C помощью кнопки "Сохранение координат" в меню "Телепортация по координатам" можно сохранить текущую позицию ГГ, а затем переместиться в эту сохранённую точку из любого места. Точек можно сохранять сколько угодно - хотел сделать лимит, но не стал...

Мои благодарности:
	-- GSC - за замечательную игру;
	-- авторам мода АМК - за некоторые скриптовые функции и арт "булыжник";
	-- proger_Dencheek - так же за некоторые функции;
	-- авторам Position Informer'а (V.I.R.U.S. и Skunk) - за отличную программу;
	-- сообществу gsc_stalker на spaces.ru (http://spaces.ru/soo/gsc_stalker)

Установка: скопировать папку gamedata в папку с чистой игрой, если спросят - согласиться на замену файлов. Новая игра не требуется.

>>>>>  Совмещение со своим модом:  <<<<<

Скопировать:
	- скрипты:	gamedata\scripts - все файлы, кроме bind_stalker.script
	- конфиги:	gamedata\config\ui - все файлы, кроме message_box.xml
				gamedata\config\misc - всё
				gamedata\config\text\rus - файл ui_st_teleport.xml
	- модели:	gamedata\meshes - всё
	- текстуры:	gamedata\textures - папку teleport

Совместить:
	>>> скрипты:
	-- в bind_stalker.script в функции actor_binder:net_spawn(data) в самом начале добавить:
		spawn_level_changer.del_old_teleport()
	в той же функции в конце, перед return true добавить:
		teleportator.spawn_teleportator()
		
	в функции actor_binder:net_destroy() ниже self.object:set_callback(callback.take_item_from_box, nil) добавить:
		self.object:set_callback(callback.use_object, nil)
		
	в функции actor_binder:reinit() ниже self.object:set_callback(callback.take_item_from_box, self.take_item_from_box, self) дописать:
		self.object:set_callback(callback.use_object, self.on_use_object, self)
		self.object:set_callback(callback.death, self.death_callback, self)
		
	выше function actor_binder:take_item_from_box(box, item) создать две новые функции:
function actor_binder:death_callback(victim, who)
	if victim:id() == db.actor:id() then
		teleportator.stop_hud()
	end
end
function actor_binder:on_use_object(obj, who)
	teleportator.use_tele(obj)
end
	
	в функции actor_binder:update(delta) в самом конце (перед последним end) дописать:
		tele_to_coord.show_pos()
		
	
	>>> конфиги:
	-- в system.ltx (gamedata\config) в секции [texture_desc] добавить после ui_asus_intro через запятую:
		ui_tele_hud
	а в конце добавить инклуд:
		#include "misc\uni_teleport.ltx"
	
	-- в info_portions.xml (gamedata\config\gameplay) добавить новые инфопоршены:
	<info_portion id="actor_give_teleport"></info_portion>
	<info_portion id="teleport_on_surfaces">
		<disable>teleport_under_ground</disable>
	</info_portion>
	<info_portion id="teleport_under_ground">
		<disable>teleport_on_surfaces</disable>
	</info_portion>
	
	-- в ui_st_other.xml (gamedata\config\text\rus) в самом конце, перед </string_table> добавить инклуд:
	#include "text\rus\ui_st_teleport.xml"
	
	-- в message_box.xml (gamedata\config\ui) так же добавить инклуд, в конце перед </window>:
	#include "ui\message_box_teleport.xml"
	
	в файле ui_custom_msgs.xml (gamedata\config\ui) в конце, перед </header> добавить:
	<hud_show_position x="10" y="250" width="300" height="100" complex_mode="1">
		<text font="graffiti22"  r="0" g="255" b="160" a="255" align="1"/>
	</hud_show_position>

	>>> текстуры: gamedata\textures\ui\ui_icon_equipment.dds - добавить иконки для телепотратора и артефакта. И, соответственно, прописать их в конфиге (gamedata\config\misc\uni_teleport.ltx)

З.Ы.: Создавался мод на широкоформате, по этому, как он будет выглядеть на простых мониторах - даже не знаю...

На этом всё. Приятной игры!

naxac©2013