#!/usr/bin/python3
# Casting Time, Range, Components, Duration, Description
choices = {
        'Burning Hands':              ['1 Action',      'Self (15 ft cone)'  ,  'V, S',    'Instantaneous',                'As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips.\nEach creature in a 15-foot cone must make a Dexterity saving throw.\nA creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one.\nThe fire ignites any flammable objects in the area that aren\'t being worn or carried.'],
        'Catapult':                   ['1 Action',      '60 ft',                'S',       'Instantaneous',                'Choose one object weighing 1 to 5 pounds within range that isn’t being worn or carried.\nThe object flies in a straight line up to 90 feet in a direction you choose before falling to the ground, stopping early if it impacts against a solid surface.\nIf the object would strike a creature, that creature must make a Dexterity saving throw.\nOn a failed save, the object strikes the target and stops moving.\nWhen the object strikes something, the object and what it strikes each take 3d8 bludgeoning damage.'],
        'Charm Person':               ['1 Action',      '30 ft',                'V, S',    '1 Hour',                       'You attempt to charm a humanoid you can see within range.\nIt must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it.\nIf it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it.\nThe charmed creature regards you as a friendly acquaintance.\nWhen the spell ends, the creature knows it was charmed by you.'],
        'Chromatic Orb':              ['1 Action',      '90 ft',                'V, S, M*','Instantaneous',                'You hurl a 4-inch-diameter sphere of energy at a creature that you can see within range.\nYou choose acid, cold, fire, lightning, poison, or thunder for the type of orb you create, and then make a ranged spell attack against the target.\nIf the attack hits, the creature takes 3d8 damage of the type you chose.\n\n* - (a diamond worth at least 50 gp)'],
        'Color Spray':                ['1 Action',      'Self (15 ft cone)',    'V, S, M*','1 Round',                      'A dazzling array of flashing, colored light springs from your hand.\nRoll 6d10; the total is how many hit points of creatures this spell can affect.\nCreatures in a 15-foot cone originating from you are affected in ascending order of their current hit points (ignoring unconscious creatures and creatures that can\'t see).\nStarting with the creature that has the lowest current hit points, each creature affected by this spell is blinded until the end of your next turn.\nSubtract each creature\'s hit points from the total before moving on to the creature with the next lowest hit points.\nA creature\'s hit points must be equal to or less than the remaining total for that creature to be affected.\n\n* - (a pinch of powder or sand that is colored red, yellow, and blue)'],
        'Earth Tremor':               ['1 Action',      '10 ft',                'V, S',    'Instantaneous',                'You cause a tremor in the ground within range.\nEach creature other than you in that area must make a Dexterity saving throw.\nOn a failed save, a creature takes 1d6 bludgeoning damage and is knocked prone.\nIf the ground in that area is loose earth or stone, it becomes difficult terrain until cleared, with each 5-foot-diameter portion requiring at least 1 minute to clear by hand.'],
        'Ice Knife':                  ['1 Action',      '60 ft (5 ft sphere)',  'S, M*',   'Instantaneous',                'You create a shard of ice and fling it at one creature within range.\nMake a ranged spell attack against the target.\nOn a hit, the target takes 1d10 piercing damage. \nHit or miss, the shard then explodes.\nThe target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 cold damage.\n\n* - (a drop of water or a piece of ice)'],
        'Magic Missile':              ['1 Action',      '120 ft',               'V, S',    'Instantaneous',                'You create three glowing darts of magical force.\nEach dart hits a creature of your choice that you can see within range.\nA dart deals 1d4 + 1 force damage to its target.\nThe darts all strike simultaneously, and you can direct them to hit one creature or several.'],
        'Ray of Sickness':            ['1 Action',      '60 ft',                'V, S',    'Instantaneous',                'A ray of sickening greenish energy lashes out toward a creature within range.\nMake a ranged spell attack against the target.\nOn a hit, the target takes 2d8 poison damage and must make a Constitution saving throw.\nOn a failed save, it is also poisoned until the end of your next turn.'],
        'Sleep':                      ['1 Action',      '90 ft (20 ft sphere)', 'V, S, M*','1 Minute',                     'This spell sends creatures into a magical slumber.\nRoll 5d8; the total is how many hit points of creatures this spell can affect.\nCreatures within 20 feet of a point you choose within range are affected in ascending order of their current hit points (ignoring unconscious creatures).\nStarting with the creature that has the lowest current hit points, each creature affected by this spell falls unconscious until the spell ends, the sleeper takes damage, or someone uses an action to shake or slap the sleeper awake.\nSubtract each creature\'s hit points from the total before moving on to the creature with the next lowest hit points.\nA creature\'s hit points must be equal to or less than the remaining total for that creature to be affected.\nUndead and creatures immune to being charmed aren\'t affected by this spell.\n\n* - (a pinch of fine sand, rose petals, or a cricket)'],
        'Thunderwave':                ['1 Action',      'Self (15 ft Cube)',    'V, S',    'Instantaneous',                'A wave of thunderous force sweeps out from you.\nEach creature in a 15-foot cube originating from you must make a Constitution saving throw.\nOn a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you.\nOn a successful save, the creature takes half as much damage and isn\'t pushed.\nIn addition, unsecured objects that are completely within the area of effect are automatically pushed 10 feet away from you by the spell\'s effect, and the spell emits a thunderous boom audible out to 300 feet.'],
        'Witch Bolt':                 ['1 Action',      '30 ft',                'V, S, M*','Concentration, up to 1 minute','A beam of crackling, blue energy lances out toward a creature within range, forming a sustained arc of lightning between you and the target.\nMake a ranged spell attack against that creature.\nOn a hit, the target takes 1d12 lightning damage, and on each of your turns for the duration, you can use your action to deal 1d12 lightning damage to the target automatically.\nThe spell ends if you use your action to do anything else.\nThe spell also ends if the target is ever outside the spell\’s range or if it has total cover from you.\n\n* - (a twig from a tree that has been struck by lightning)'],
        #                __
        # Level 2 Spells \/
        'Aganazzar\'s Scorcher':      ['1 Action',      '30 ft (30 ft arrow)',  'V, S, M*','Instantaneous',                'A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose.\nEach creature in the line must make a Dexterity saving throw.\nA creature takes 3d8 fire damage on a failed save, or half as much damage on a successful one.\n\n* - (a red dragon\'s scale)'],
        'Blindness/Deafness':         ['1 Action',      '30 ft',                'V',       '1 Minute',                     'You can blind or deafen a foe.\nChoose one creature that you can see within range to make a Constitution saving throw. If it fails, the target is either blinded or deafened (your choice) for the duration.\nAt the end of each of its turns, the target can make a Constitution saving throw. On a success, the spell ends.'],
        'Cloud of Daggers':           ['1 Action',      '60 ft',                'V, S, M*','Concentration, up to 1 minute','You fill the air with spinning daggers in a cube 5 feet on each side, centered on a point you choose within range. A creature takes 4d4 slashing damage when it enters the spell\'s area for the first time on a turn or starts its turn there.\n\nAt Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 2d4 for each slot level above 2nd.\n\n* - (a sliver of glass)'],
        'Crown of Madness':           ['1 Action',      '120 ft',               'V, S',    'Concentration, up to 1 minute','One humanoid of your choice that you can see within range must succeed on a W isdom  saving throw or becom e charmed by you for the duration. While the target is charmed in this way, a twisted crown of jagged iron appears on its head, and a madness glows in its eyes.\n\nThe charmed target must use its action before moving on each of its turns to make a melee attack against a creature other than itself that you mentally choose.\n\nThe target can act normally on its turn if you choose no creature or if none are within its reach.\n\nOn your subsequent turns, you must use your action to maintain control over the target, or the spell ends. Also, the target can make a W isdom saving throw at the end of each of its turns. On a success, the spell ends.'],
        'Dust Devil':                 ['1 Action',      '60 ft',                'V, S, M*','1 Minute',                     'Choose an unoccupied 5-foot cube of air that you can see within range.\nAn elemental force that resembles a dust devil appears in the cube and lasts for the spell’s duration.\nAny creature that ends its turn within 5 feet of the dust devil must make a Strength saving throw.\nOn a failed save, the creature takes 1d8 bludgeoning damage and is pushed 10 feet away. On a successful save, the creature takes half as much damage and isn’t pushed.\nAs a bonus action, you can move the dust devil up to 30 feet in any direction.\nIf the dust devil moves over sand, dust, loose dirt, or small gravel, it sucks up the material and forms a 10-foot-radius cloud of debris around itself that lasts until the start of your next turn. The cloud heavily obscures its area.\n\n* - (a pinch of dust)'],
        'Earthbind':                  ['1 Action',      '300 ft',               'V',       '1 Minute',                     'Choose one creature you can see within range. Yellow strips of magical energy loop around the creature. The target must succeed on a Strength saving throw, or its flying speed (if any) is reduced to 0 feet for the spell’s duration. An airborne creature affected by this spell safely descends at 60 feet per round until it reaches the ground or the spell ends.'],
        'Enlarge/Reduce':             ['1 Action',      '30 ft',                'V, S, M*','1 Minute',                     'You cause a creature or an object you can see within range to grow larger or smaller for the duration. Choose either a creature or an object that is neither worn nor carried. If the target is unwilling, it can make a Constitution saving throw. On a success, the spell has no effect.\n\nIf the target is a creature, everything it is wearing and carrying changes size with it. Any item dropped by an affected creature returns to normal size at once.\n\n\nEnlarge. The target\'s size doubles in all dimensions, and its weight is multiplied by eight. This growth increases its size by one category-- from Medium to Large, for example. If there isn\'t enough room for the target to double its size, the creature or object attains the maximum possible size in the space available. Until the spell ends, the target also has advantage on Strength checks and Strength saving throws. The target\'s weapons also grow to match its new size. While these weapons are enlarged, the target\'s attacks with them deal 1d4 extra damage.\n\nReduce. The target\'s size is halved in all dimensions, and its weight is reduced to one-eighth of normal. This reduction decreases its size by one category--from Medium to Small, for example. Until the spell ends, the target also has disadvantage on Strength checks and Strength saving throws. The target\'s weapons also shrink to match its new size. While these weapons are reduced, the target\'s attacks with them deal 1d4 less damage (this can\'t reduce the damage below 1).\n\n* - (a pinch of powdered iron)'],
        'Gust of Wind':               ['1 Action',      'self',                 'V, S, M*','1 Minute',                     'A line of strong wind 60 feet long and 10 feet wide blasts from you in a direction you choose for the spell\'s duration. Each creature that starts its turn in the line must succeed on a Strength saving throw or be pushed 15 feet away from you in a direction following the line.\n\nAny creature in the line must spend 2 feet of movement for every 1 foot it moves when moving closer to you.\n\nThe gust disperses gas or vapor, and it extinguishes candles, torches, and similar unprotected flames in the area. It causes protected flames, such as those of lanterns, to dance wildly and has a 50 percent chance to extinguish them.\n\nAs a bonus action on each of your turns before the spell ends, you can change the direction in which the line blasts from you.\n\n* - (a legume seed)'],
        'Hold Person':                ['1 Action',      '60 ft',                'V, S, M*','1 Minute',                     'Choose a humanoid that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration. At the end of each of its turns, the target can make another Wisdom saving throw. On a success, the spell ends on the target.\n\nAt Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, you can target one additional humanoid for each slot level above 2nd. The humanoids must be within 30 feet of each other when you target them.\n\n* - (a small, straight piece of iron)'],
        'Maximilian\'s Earthen Grasp':['1 Action',      '30 ft (5 ft square)',  'V, S, M*','1 Minute',                     'You choose a 5-foot-square unoccupied space on the ground that you can see within range. A Medium hand made from compacted soil rises there and reaches for one creature you can see within 5 feet of it. The target must make a Strength saving throw. On a failed save, the target takes 2d6 bludgeoning damage and is <a href="https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Restrained">restrained</a> for the spell’s duration.\n\nAs an action, you can cause the hand to crush the <a href="https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Restrained">restrained</a> target, who must make a Strength saving throw. It takes 2d6 bludgeoning damage on a failed save, or half as much damage on a successful one.\n\nTo break out, the <a href="https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Restrained">restrained</a> target can make a Strength check against your spell save DC. On a success, the target escapes and is no longer <a href="https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Restrained">restrained</a> by the hand.\n\nAs an action, you can cause the hand to reach for a different creature or to move to a different unoccupied space within range. The hand releases a <a href="https://www.dndbeyond.com/sources/basic-rules/appendix-a-conditions#Restrained">restrained</r> target if you do either.\n\n* - (a miniature hand sculpted from clay)'],
        'Phantasmal Force':           ['1 Action',      '60 ft',                'V, S, M*','Concentration, up to 1 minute','You craft an illusion that takes root in the mind of a creature that you can see within range.\nThe target must make an Intelligence saving throw.\n\nOn a failed save, you create a phantasmal object, creature, or other visible phenomenon of your choice that is no larger than a 10-foot cube and that is perceivable only to the target for the duration.\nThis spell has no effect on undead or constructs.\nThe phantasm includes sound, temperature, and other stimuli, also evident only to the creature.\nThe target can use its action to examine the phantasm with an Intelligence (Investigation) check against your spell save DC.\n\nIf the check succeeds, the target realizes that the phantasm is an illusion, and the spell ends.\n\nWhile a target is affected by the spell, the target treats the phantasm as if it were real.\nThe target rationalizes any illogical outcomes from interacting with the phantasm.\n\nFor example, a target attempting to walk across a phantasmal bridge that spans a chasm falls once it steps onto the bridge.\nIf the target survives the fall, it still believes that the bridge exists and comes up with some other explanation for its fall: it was pushed, it slipped, or a strong wind might have knocked it off.\nAn affected target is so convinced of the phantasm’s reality that it can even take damage from the illusion.\nA phantasm created to appear as a creature can attack the target.\nSimilarly, a phantasm created to appear as fire, a pool of acid, or lava can burn the target.\nEach round on your turn, the phantasm can deal 1d6 psychic damage to the target if it is in the phantasm’s area or within 5 feet of the phantasm, provided that the illusion is of a creature or hazard that could logically deal damage, such as by attacking.\nThe target perceives the damage as a type appropriate to the illusion.\n\n* - (a bit of fleece)'],
        'Pyrotechnics':               ['1 Action',      '60 ft (5 ft cube)',    'V, S',    'Instantaneous',                'Choose an area of nonmagical flame that you can see and that fits within a 5-foot cube within range. You can extinguish the fire in that area, and you create either fireworks or smoke when you do so.\n\nFireworks. The target explodes with a dazzling display of colors. Each creature within 10 feet of the target must succeed on a Constitution saving throw or become blinded until the end of your next turn.\n\nSmoke. Thick black smoke spreads out from the target in a 20-foot radius, moving around corners. The area of the smoke is heavily obscured. The smoke persists for 1 minute or until a strong wind disperses it.'],
        'Scorching Ray':              ['1 Action',      '120 ft',               'V, S',    'Instantaneous',                'You create three rays of fire and hurl them at targets within range. You can hurl them at one target or several.\n\nMake a ranged spell attack for each ray. On a hit, the target takes 2d6 fire damage.\n\nAt Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, you create one additional ray for each slot level above 2nd.'],
        'Shatter':                    ['1 Action',      '60 ft (10 ft sphere)', 'V, S, M*','Instantaneous',                'A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range.\nEach creature in a 10-foot-radius sphere centered on that point must make a Constitution saving throw.\nA creature takes 3d8 thunder damage on a failed save, or half as much damage on a successful one.\nA creature made of inorganic material such as stone, crystal, or metal has disadvantage on this saving throw.\nA nonmagical object that isn\'t being worn or carried also takes the damage if it\'s in the spell\'s area.\n\n* - (a chip of mica)'],
        'Snilloc\s Snowball Swarm':   ['1 Action',      '90 ft (5 ft Sphere)',  'V, S, M*','Instantaneous',                'A flurry of magic snowballs erupts from a point you choose within range. Each creature in a 5-foot-radius sphere centered on that point must make a Dexterity saving throw. A creature takes 3d6 cold damage on a failed save, or half as much damage on a successful one.\n\n* - (a piece of ice or a small white rock chip)'],
        'Suggestion':                 ['1 Action',      '30 ft',                'V, M*',   '8 Hours',                      'You suggest a course of activity (limited to a sentence or two) and magically influence a creature you can see within range that can hear and understand you.\nCreatures that can\'t be charmed are immune to this effect.\nThe suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to stab itself, throw itself onto a spear, immolate itself, or do some other obviously harmful act ends the spell.\nThe target must make a Wisdom saving throw. On a failed save, it pursues the course of action you described to the best of its ability. The suggested course of action can continue for the entire duration.\nIf the suggested activity can be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.\nYou can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that a knight give her warhorse to the first beggar she meets.\nIf the condition isn\'t met before the spell expires, the activity isn\'t performed.\nIf you or any of your companions damage the target, the spell ends.\n\n* - (a snake\'s tongue and either a bit of honeycomb or a drop of sweet oil)'],
        'Web':                        ['1 Action',      '60 ft (20 ft cube)',   'V, S, M*','1 Hour',                       'You conjure a mass of thick, sticky webbing at a point of your choice within range. The webs fill a 20- foot cube from that point for the duration. The webs are difficult terrain and lightly obscure their area.\nIf the webs aren\'t anchored between two solid masses (such as walls or trees) or layered across a floor, wall, or ceiling, the conjured web collapses on itself, and the spell ends at the start of your next turn. Webs layered over a flat surface have a depth of 5 feet.\nEach creature that starts its turn in the webs or that enters them during its turn must make a Dexterity saving throw. On a failed save, the creature is restrained as long as it remains in the webs or until it breaks free.\nA creature restrained by the webs can use its action to make a Strength check against your spell save DC. If it succeeds, it is no longer restrained.\nThe webs are flammable. Any 5-foot cube of webs exposed to fire burns away in 1 round, dealing 2d4 fire damage to any creature that starts its turn in the fire.\n\n* - (a bit of spiderweb)']
        }
# Casting Time, Range, Components, Duration, Description
