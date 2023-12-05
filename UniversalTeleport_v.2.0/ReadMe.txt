====================================================
��������:	Universal Teleport v 2.0
���������:	S.T.A.L.K.E.R. ���� ��������� 1.0004
�����:		naxac
====================================================
��� ��������� � ���� ������ ������������, � ������� �������� ����� ������������� � ����� ����� ����. ��� ����� ������ ������ ������� �����������, ��������� �� �������� �����. ������������ ������ ����� �������������� ���������� ���, �� ��� ��� ������������� ���������� ����� ��� ���� ����� ��������. ����� ������������� (�����������) �������� ����������� � "��������" - ���� ���, �� ������� � ��� ������ �������.
������ ���������� � ��������� � ����� ������ ����.
� ������� ���� "������������ �� �����������" ����� ������������� � ����� ����� � �������� �������, �� ������� � ������ ������ ��������� ��. ���������� - ��� ��� ������� - � ��� �� ����.
C ������� ������ "���������� ���������" � ���� "������������ �� �����������" ����� ��������� ������� ������� ��, � ����� ������������� � ��� ���������� ����� �� ������ �����. ����� ����� ��������� ������� ������ - ����� ������� �����, �� �� ����...

��� �������������:
	-- GSC - �� ������������� ����;
	-- ������� ���� ��� - �� ��������� ���������� ������� � ��� "��������";
	-- proger_Dencheek - ��� �� �� ��������� �������;
	-- ������� Position Informer'� (V.I.R.U.S. � Skunk) - �� �������� ���������;
	-- ���������� gsc_stalker �� spaces.ru (http://spaces.ru/soo/gsc_stalker)

���������: ����������� ����� gamedata � ����� � ������ �����, ���� ������� - ����������� �� ������ ������. ����� ���� �� ���������.

>>>>>  ���������� �� ����� �����:  <<<<<

�����������:
	- �������:	gamedata\scripts - ��� �����, ����� bind_stalker.script
	- �������:	gamedata\config\ui - ��� �����, ����� message_box.xml
				gamedata\config\misc - ��
				gamedata\config\text\rus - ���� ui_st_teleport.xml
	- ������:	gamedata\meshes - ��
	- ��������:	gamedata\textures - ����� teleport

����������:
	>>> �������:
	-- � bind_stalker.script � ������� actor_binder:net_spawn(data) � ����� ������ ��������:
		spawn_level_changer.del_old_teleport()
	� ��� �� ������� � �����, ����� return true ��������:
		teleportator.spawn_teleportator()
		
	� ������� actor_binder:net_destroy() ���� self.object:set_callback(callback.take_item_from_box, nil) ��������:
		self.object:set_callback(callback.use_object, nil)
		
	� ������� actor_binder:reinit() ���� self.object:set_callback(callback.take_item_from_box, self.take_item_from_box, self) ��������:
		self.object:set_callback(callback.use_object, self.on_use_object, self)
		self.object:set_callback(callback.death, self.death_callback, self)
		
	���� function actor_binder:take_item_from_box(box, item) ������� ��� ����� �������:
function actor_binder:death_callback(victim, who)
	if victim:id() == db.actor:id() then
		teleportator.stop_hud()
	end
end
function actor_binder:on_use_object(obj, who)
	teleportator.use_tele(obj)
end
	
	� ������� actor_binder:update(delta) � ����� ����� (����� ��������� end) ��������:
		tele_to_coord.show_pos()
		
	
	>>> �������:
	-- � system.ltx (gamedata\config) � ������ [texture_desc] �������� ����� ui_asus_intro ����� �������:
		ui_tele_hud
	� � ����� �������� ������:
		#include "misc\uni_teleport.ltx"
	
	-- � info_portions.xml (gamedata\config\gameplay) �������� ����� �����������:
	<info_portion id="actor_give_teleport"></info_portion>
	<info_portion id="teleport_on_surfaces">
		<disable>teleport_under_ground</disable>
	</info_portion>
	<info_portion id="teleport_under_ground">
		<disable>teleport_on_surfaces</disable>
	</info_portion>
	
	-- � ui_st_other.xml (gamedata\config\text\rus) � ����� �����, ����� </string_table> �������� ������:
	#include "text\rus\ui_st_teleport.xml"
	
	-- � message_box.xml (gamedata\config\ui) ��� �� �������� ������, � ����� ����� </window>:
	#include "ui\message_box_teleport.xml"
	
	� ����� ui_custom_msgs.xml (gamedata\config\ui) � �����, ����� </header> ��������:
	<hud_show_position x="10" y="250" width="300" height="100" complex_mode="1">
		<text font="graffiti22"  r="0" g="255" b="160" a="255" align="1"/>
	</hud_show_position>

	>>> ��������: gamedata\textures\ui\ui_icon_equipment.dds - �������� ������ ��� ������������� � ���������. �, ��������������, ��������� �� � ������� (gamedata\config\misc\uni_teleport.ltx)

�.�.: ���������� ��� �� �������������, �� �����, ��� �� ����� ��������� �� ������� ��������� - ���� �� ����...

�� ���� ��. �������� ����!

naxac�2013