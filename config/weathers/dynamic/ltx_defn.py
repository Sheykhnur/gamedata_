# LTX definitions for prettyfier
# Lost Alpha version
# for any other STALKER game, you need to update this

import re

weaponParamGroups = [
	[
		"Inventory icon",
		[
			"inv_grid_width",
			"inv_grid_height",
			"inv_grid_x",
			"inv_grid_y",
			"scope_x",
			"scope_y",
			"grenade_launcher_x",
			"grenade_launcher_y",
			"silencer_x",
			"silencer_y",
		],
	],
	[
		"Text",
		[
			"inv_name",
			"inv_name_short",
			"description",
		],
	],
	[
		"Visual",
		[
			"attach_angle_offset",
			"attach_bone_name",
			"attach_position_offset",
			"angle_offset",
			"bone_name",
			"grenade_bone",
			"hud",
			"position",
			"position_offset",
			"orientation",
			"direction",
			"normal",
			"icon",
			"scope_texture",
			"strap_position",
			"strap_orientation",
			"strap_bone0",
			"strap_bone1",
			"visual",
			"lens_texture",
			"lens_texture_h",
			"lens_texture_w",
			"lens_texture_x",
			"lens_texture_y",
		],
	],
	[
		"Effects",
		[
			"fire_point",
			"fire_point2",
			"flame_particles",
			"smoke_particles",
			"grenade_flame_particles",
			"silencer_smoke_particles",
			"shell_point",
			"shell_dir",
			"shell_particles",
			"light_disabled",
			"light_color",
			"light_range",
			"light_var_color",
			"light_var_range",
			"light_time",
			"silencer_light_color",
			"silencer_light_range",
			"silencer_light_var_color",
			"silencer_light_var_range",
			"silencer_light_time",
			"throw_point",
			"explode_duration",
			"explode_particles",
			"wallmark_section",
			"wm_size",
		],
	],
	[
		"Sounds",
		[
			"snd_reload_grenade",
			"snd_shoot_grenade",
			"snd_switch",
			r"snd_.+",
			# "snd_gyro",
			# "snd_zoomin",
			# "snd_zoomout",
			# "snd_draw",
			# "snd_holster",
			# "snd_empty",
			# "snd_checkout",
			# "snd_explode",
			# "snd_shoot",
			# "snd_shoot1",
			# "snd_shoot_1",
			# "snd_shoot2",
			# "snd_shoot3",
			# "snd_shoot4",
			# "snd_shoot5",
			# "snd_shoot6",
			# "snd_shoot7",
			# "snd_shoot8",
			# "snd_shoot_duplet",
			# "snd_shoot_grenade",
			# "snd_silncer_shot",
			# "snd_reload",
			# "snd_reload_1",
			# "snd_reload_grenade",
			# "snd_switch",
			# "snd_bore",
			# "snd_bore1",
			# "snd_bore2",
			# "snd_close",
		],
	],
	[
		"Upgrade icon",
		[
			"upgr_icon",
			"upgr_icon_x",
			"upgr_icon_y",
			"upgr_icon_width",
			"upgr_icon_height",
		],
	],
	[
		"Cost & Weight",
		[
			"cost",
			"inv_weight",
			"ph_mass",
		],
	],
	[
		"Ammo",
		[
			"ammo_limit",
			"ammo_class",
			"ammo_elapsed",
			"ammo_mag_size",
			"grenade_class",
		],
	],
	[
		"Features",
		[
			"fire_modes",
			"scope_name",
			"scopes_sect",
			"scope_status",
			"scope_alive_detector",
			"scope_nightvision",
			"scope_dynamic_zoom",
			"scope_zoom_factor",
			"silencer_name",
			"silencer_status",
			"grenade_launcher_name",
			"grenade_launcher_status",
			"tri_state_reload",
		],
	],
	[
		"Impact",
		[
			"hit_power",
			"hit_power_critical",
			"hit_impulse",
			"hit_type",
			"hit_power_2",
			"hit_power_critical_2",
			"hit_impulse_2",
			"hit_type_2",
			"hit_type_blast",
			"hit_type_frag",
			"hit_probability_gd_master",
			"hit_probability_gd_novice",
			"hit_probability_gd_stalker",
			"hit_probability_gd_veteran",
			"detonation_threshold_hit",
			"frags",
			"frags_r",
			"frag_hit",
			"frag_hit_impulse",
			"fragment_speed",
			"blast",
			"blast_r",
			"blast_impulse",
			"blast_impulse_factor",
		]
	],
	[
		"Ballistics",
		[
			"air_resistance_factor",
			"bullet_speed",
			"launch_speed",
			"grenade_vel",
			"fire_distance",
			"fire_direction_offset",
			"fire_dispersion_base",
			"fire_dispersion_condition_factor",
			"force_const",
			"force_grow_speed",
			"force_max",
			"force_min",
			"throw_dir",
			"up_throw_factor",
		],
	],
	[
		"Performance",
		[
			"rpm",
			"rpm_no_disp",
			"rpm_semi",
			"rpm_empty_click",
			"shot_max_delay",
			"use_aim_bullet",
			"time_to_aim",
		],
	],
	[
		"Reliability",
		[
			"misfire_probability",
			"misfire_start_condition",
			"misfire_end_condition",
			"misfire_start_prob",
			"misfire_end_prob",
			"condition_shot_dec",
			"condition_queue_shot_dec",
		],
	],
	[
		"Handling",
		[
			"control_inertion_factor",
			"crosshair_inertion",
			"PDM_disp_base",
			"PDM_disp_vel_factor",
			"PDM_disp_accel_factor",
			"PDM_disp_crouch",
			"PDM_disp_crouch_no_acc",
			"sprint_allowed",
		],
	],
	[
		"Recoil",
		[
			"cam_return",
			"cam_relax_speed",
			"cam_relax_speed_ai",
			"cam_dispersion",
			"cam_dispersion_inc",
			"cam_dispersion_frac",
			"cam_max_angle",
			"cam_max_angle_horz",
			"cam_step_angle_horz",
			"zoom_cam_relax_speed",
			"zoom_cam_relax_speed_ai",
			"zoom_cam_dispersion",
			"zoom_cam_dispersion_inc",
			"zoom_cam_dispersion_frac",
			"zoom_cam_max_angle",
			"zoom_cam_max_angle_horz",
			"zoom_cam_step_angle_horz",
			"dispersion_start",
		],
	],
	[
		"Aiming",
		[
			"zoom_enabled",
			"zoom_dof",
			"zoom_hide_crosshair",
			"zoom_inertion_factor",
			"zoom_rotate_time",
			"max_zoom_factor",
			"reload_dof",
			"ezi_camera_move_epsilon",
			"ezi_disp_min",
			"ezi_speed_min",
			"ezi_zoom_aim_disp_k",
			"ezi_zoom_aim_speed_k",
			"ezi_delta_time",
		],
	],
	[
		"Upgrades",
		[
			"upgrade_scheme",
			"upgrades",
			"installed_upgrades",
		],
	],
	[
		"AI Params",
		[
			"min_radius",
			"max_radius",
			"holder_range_modifier",
			"holder_fov_modifier",
		],
	],
]

flaresParamGroups = [
	[
		"main",
		[
			"flare_textures",
			"flare_position",
			"flare_radius",
			"flare_opacity",
			"flare_shader",
			"flares",
			"gradient",
			"gradient_opacity",
			"gradient_radius",
			"gradient_shader",
			"gradient_texture",
			"source",
			"source_radius",
			"source_texture",
			"source_shader",
			"source_ignore_color",
			"blend_time",
			"blend_rise_time",
			"blend_down_time",
		],
	],
]

weatherParamGroups = [
	[
		"Sky",
		[
			"sky_texture",
			"sky_rotation",
			"sky_color",
		],
	],
	[
		"Clouds",
		[
			"clouds_texture",
			"clouds_color",
			"clouds_velocity_0",
			"clouds_velocity_1",
		],
	],
	[
		"Colors and sun",
		[
			"hemi_color",
			"ambient",
			"sun_color",
			"sun_shafts_intensity",
			"flares",
		],
	],
	[
		"Fog and farplane",
		[
			"far_plane",
			"fog_distance",
			"fog_color",
			"fog_density",
		],
	],
	[
		"Dof settings",
		[
			"dof",
			"dof_kernel",
			"dof_sky",
		],
	],
	[
		"Sounds",
		[
			"env_ambient",
		],
	],
	[
		"Rain and water",
		[
			"rain_density",
			"rain_color",
			"water_intensity",
		],
	],
	[
		"Wind",
		[
			"wind_velocity",
			"wind_direction",
			"wind_sound_volume",
			"trees_amplitude",
			"swing_normal_amp1",
			"swing_normal_amp2",
			"swing_normal_rot1",
			"swing_normal_rot2",
			"swing_normal_speed",
			"swing_fast_amp1",
			"swing_fast_amp2",
			"swing_fast_rot1",
			"swing_fast_rot2",
			"swing_fast_speed",
		],
	],
	[
		"Thunderbolt",
		[
			"thunderbolt",
			"bolt_duration",
			"bolt_period",
		],
	],
]

ammoParamGroups = [
	[
		"Appearance",
		[
			"visual",
			"explosive",
			"tracer",
			"tracer_color_ID",
			"wm_size",
		],
	],
	[
		"Icon",
		[
			"inv_grid_width",
			"inv_grid_height",
			"inv_grid_x",
			"inv_grid_y",
		],
	],
	[
		"Text",
		[
			"inv_name",
			"inv_name_short",
			"description",
		],
	],
	[
		"Economy",
		[
			"cost",
			"inv_weight",
			"box_size",
			"belt",
		],
	],
	[
		"Impact",
		[
			"k_hit",
			"k_ap",
			"k_pierce",
			"k_impulse",
			"allow_ricochet",
			"impair",
			"buck_shot",
		],
	],
	[
		"Ballistics",
		[
			"k_air_resistance",
			"k_disp",
			"k_dist",
			"k_speed",
		],
	],
]

def isWeaponSect(name):
	return re.match(r'^(wpn_|weapon_|hands|static_mg).*$(?<!_hud)', name)

allDefinitions = [
	{
		"name": "weapon",
		"selector": lambda sect: isWeaponSect(sect['name']) or any(s for s in sect['inherit'] if isWeaponSect(s)),
		"groups": weaponParamGroups,
		"deleteKeys": [
			"ammo_current",
			"startup_ammo",
			"scopes",
			"parent_section",
			"kill_msg_width",
			"kill_msg_height",
			"kill_msg_x",
			"kill_msg_y",
			"silencer_hit_power",
			"silencer_hit_impulse",
			"silencer_fire_distance",
			"silencer_bullet_speed",
		]
	},
	{
		"name": "weather",
		"selector": lambda sect: re.match(r'^default_', sect['name']),
		"groups": weatherParamGroups,
		"deleteKeys": [
			"lmap_color",
			"sun_lumscale",
			"sun_dir",
			"sun_longitude",
			"sun_altitude",
			"dof_plane",
			"dof_speed",
		]
	},
	{
		"name": "flares",
		"selector": lambda sect: re.match(r'^flares_', sect['name']),
		"groups": flaresParamGroups,
		"deleteKeys": []
	},
	{
		"name": "ammo",
		"selector": lambda sect: re.match(r'^ammo_', sect['name']),
		"groups": ammoParamGroups,
		"deleteKeys": []
	},
]


for defn in allDefinitions:
	defn['allKeys'] = {
		item: True
		for group in defn['groups']
			for item in group[1]
	}

