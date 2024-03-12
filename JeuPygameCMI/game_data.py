from pathing import path

#palmiers, 1 :
level_0 = {
		'name':'level_0',
		'next_level':'level_2',
		'terrain': path+'/levels/lvl0/0/level_0._terrain.csv',
		'coins': path+'/levels/lvl0/0/level_0._coins.csv',
		'fg palms':path+'/levels/lvl0/0/level_0._fg_palms.csv',
		'bg palms':path+'/levels/lvl0/0/level_0._bg_palms.csv',
		'crates': path+'/levels/lvl0/0/level_0._crates.csv',
		'enemies':path+'/levels/lvl0/0/level_0._enemies.csv',
		'constraints':path+'/levels/lvl0/0/level_0._constraints.csv',
		'player': path+'/levels/lvl0/0/level_0._player.csv',
		'grass': path+'/levels/lvl0/0/level_0._grass.csv'}


#desert :
level_1 = {
		'name':'level_1',
		'next_level':'level_5',
        'terrain': './levels/lvl1/0/level_0_terrain.csv',
        'coins': './levels/lvl1/0/level_0_coins.csv',
        'crates': './levels/lvl1/0/level_0_crates.csv',
        'enemies': './levels/lvl1/0/level_0_ennemies.csv',
        'constraints': './levels/lvl1/0/level_0_blocking.csv',
        'player': './levels/lvl1/0/level_0_player.csv',
        'vegetation': './levels/lvl1/0/level_0_vegetation.csv'
}

#palmiers, 2 :
level_2 = {
	'name':'level_2',
	'next_level':'level_1',
	'terrain' : './levels/lvl2/0/level_2._terrain.csv',
	'coins'   : './levels/lvl2/0/level_2._coins.csv',
	'fg palms': './levels/lvl2/0/level_2._fg_palms.csv',
	'bg palms': './levels/lvl2/0/level_2._bg_palms.csv',
	'crates'  : './levels/lvl2/0/level_2._crates.csv',
	'enemies' : './levels/lvl2/0/level_2._enemies.csv',
	'constraints': './levels/lvl2/0/level_2._constraints.csv',
	'player'  : './levels/lvl2/0/level_2._player.csv',
	'grass'   : './levels/lvl2/0/level_2._grass.csv'
}

#prairie :
level_3 = {
	'name':'level_3',
	'next_level':'level_4',
	'terrain' : './levels/lvl3/0/level_3._terrain.csv',
	'coins'   : './levels/lvl3/0/level_3._coins.csv',
	'crates'  : './levels/lvl3/0/level_3._crates.csv',
	'enemies' : './levels/lvl3/0/level_3._enemies.csv',
	'constraints': './levels/lvl3/0/level_3._constraints.csv',
	'player'  : './levels/lvl3/0/level_3._player.csv',
	'grass'   : './levels/lvl3/0/level_3._grass.csv',
	'trees': './levels/lvl3/0/level_3._trees.csv',
	'bushes' : './levels/lvl3/0/level_3._bushes.csv'
}

#prairie, 2 :
level_4 = {
	'name':'level_4',
	'next_level':'level_6',
	'terrain' : './levels/lvl4/0/level_4_terrain_tiles.csv',
	'coins'   : './levels/lvl4/0/level_4_coin_tiles.csv',
	'crates'  : './levels/lvl4/0/level_4_crate_tiles.csv',
	'enemies' : './levels/lvl4/0/level_4_enemy_tile.csv',
	'constraints': './levels/lvl4/0/level_4_contraints.csv',
	'player'  : './levels/lvl4/0/level_4_player_tiles.csv',
	'grass'   : './levels/lvl4/0/level_4_grass_lvl3.csv',
	'trees': './levels/lvl4/0/level_4_tree_tiles.csv',
	'bushes' : './levels/lvl4/0/level_4_bush_tiles.csv'
}

#désert, 2 :
level_5 = {
		'name':'level_5',
		'next_level':'level_3',
        'terrain': './levels/lvl5/0/level_5._terrain.csv',
        'coins': './levels/lvl5/0/level_5._coins.csv',
        'crates': './levels/lvl5/0/level_5._crates.csv',
        'enemies': './levels/lvl5/0/level_5._ennemies.csv',
        'constraints': './levels/lvl5/0/level_5._blocking.csv',
        'player': './levels/lvl5/0/level_5._player.csv',
        'vegetation': './levels/lvl5/0/level_5._vegetation.csv'
}

#prairie, 3:
level_6 = {
	'name':'level_6',
	'next_level':'level_7',
	'terrain' : './levels/lvl6/0/level_6._terrain.csv',
	'coins'   : './levels/lvl6/0/level_6._coins.csv',
	'crates'  : './levels/lvl6/0/level_6._crates.csv',
	'enemies' : './levels/lvl6/0/level_6._enemies.csv',
	'constraints': './levels/lvl6/0/level_6._constraints.csv',
	'player'  : './levels/lvl6/0/level_6._player.csv',
	'grass'   : './levels/lvl6/0/level_6._grass.csv',
	'trees': './levels/lvl6/0/level_6._trees.csv',
	'bushes' : './levels/lvl6/0/level_6._bushes.csv'
}

mondes =[[level_0, level_2], [level_1, level_5], [level_3, level_4, level_6]] #Liste de monde étant eux meme une liste de niveau	

#Conformément au code pénal, le message de la ligne 107 n'est pas considéré comme subliminal car il est annoncé ici au conscient du lecteur.
progress_codes = {"level_1":"EVHGVYT37DYGH","level_2":'ENBUCEO5844', 'level_3':'AHQKerijrh4', 'level_4':'MQLeer857e52', 'level_5':'VTGzehhvD47', 'level_6':"dDZHHJ75498"}