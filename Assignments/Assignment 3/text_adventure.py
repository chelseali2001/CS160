choice = int(input("Hello and welcome to Adventure Time! Enter 1 to go right or enter 2 to go left: "))

if choice == 1:
	choice = int(input("\nYou chose right. You have entered the dragon's layer and now you have to pick between 2 mysterious potions to survive. Enter 1 to drink the red potion or enter 2 to drink the blue potion: "))

	if choice == 1:
		choice = int(input("\nYou drank the red potion and you are now invisible. Enter 1 to throw rocks at the dragon or enter 2 to distract the dragon with meat: "))

		if choice == 1:
			choice = int(input("\nYou threw rocks at the dragon and now the dragon is angry. Enter 1 to shoot fire arrows at the dragon or enter 2 to try to escape the room: "))

			if choice == 1:
				choice = int(input("\nYou killed the dragon with fire arrows. Enter 1 to steal the dragon's golden egg or enter 2 to just leave: "))

				if choice == 1:
					choice = int(input("\nYou stole the dragon's golden egg. Enter 1 to give it to the villagers back home or enter 2 to sell it: "))

					if choice == 1:
						print("You gave it to the villagers, you are now regarded as a wonderful hero and a statue of you is made in your honor! The adventure has ended.\n")
					elif choice == 2:
						print("You sold the egg and now you are the richest person in your village! The adventure has ended.\n")
				elif choice == 2:
					print("You left the dragon's layer. The villagers back home are calling you the greatest knight of all time! The adventure has ended.\n")
			elif choice == 2:
				print("You tried to escape the dragon's layer, but the dragon crushed you with its tail. The adventure has ended.\n")
		elif choice == 2:
			choice = int(input("\nYou have distracted the dragon with meat. Enter 1 to steal the dragon's golden egg or enter 2 to just leave: "))

			if choice == 1:
				choice = int(input("\nYou stole the dragon's golden egg. Enter 1 to give it to the villagers back home or enter 2 to sell it: "))

				if choice == 1:
					print("You gave it to the villagers, you are now regarded as a wonderful hero and a statue of you is made in your honor! The adventure has ended.\n")
				elif choice == 2:
					print("You sold the egg and now you are the richest person in your village! The adventure has ended.\n")
			elif choice == 2:
				print("You left the dragon's layer empty handed. The villagers back home are calling you a coward. The adventure has ended.\n")
	elif choice == 2:
		choice = int(input("\nYou drank the blue potion, you are now able to fly. Enter 1 to collapse the ceiling above the dragon or enter 2 to fly past the dragon."))

		if choice == 1:
			choice = int(input("\nYou collapsed the ceiling and now the dragon is dead. Enter 1 to steal the dragon's golden egg or enter 2 to just leave: "))

			if choice == 1:
				choice = int(input("\nYou stole the dragon's golden egg. Enter 1 to give it to the villagers back home or enter 2 to sell it: "))

				if choice == 1:
					print("You gave it to the villagers, you are now regarded as a wonderful hero and a statue of you is made in your honor! The adventure has ended.\n")
				elif choice == 2:
					print("You sold the egg and now you are the richest person in your village! The adventure has ended.\n")
			elif choice == 2:
				print("You left the dragon's layer. The villagers back home are calling you the greatest knight of all time! The adventure has ended.\n")
		elif choice == 2:
			print("You left the dragon's layer. The villagers back home are calling you a coward. The adventure has ended.\n")
elif choice == 2:
	choice = int(input("\nYou chose left. You've now encountered a goblin. Enter 1 to fight it with your sword or enter 2 to shoot it with arrows: "))

	if choice == 1:
		choice = int(input("\nYou stabbed the goblin in the leg. Enter 1 to decapitate it or enter 2 to stab it in the chest: "))

		if choice == 1:
			print("You tried to chop the goblin's head off but it hit you in the head with its club. The adventure has ended.\n")
		elif choice == 2:
			choice = int(input("\nYou stabbed the goblin in the chest and killed it. Enter 1 to bring back the goblin's gold to your village or enter 2 to bring back the goblin's magical mysterious potion to your village: "))

			if choice == 1:
				print("You brought back the goblin's gold to your village. The villagers are all very happy and have named you the new leader! The adventure has ended.\n")
			elif choice == 2:
				print("You brought back the goblin's potion to your village. Turns out it was just water but at least people are not living in fear of the goblin anymore. The adventure has ended.\n")

	elif choice == 2:
		choice = int(input("\nYou blinded the goblin with arrows. Enter 1 to escape from the goblin or enter 2 shoot it with a fire arrow: "))

		if choice == 1:
			print("You tried to escape from the goblin but the goblin hit you in the head with its club. The adventure has ended.\n")
		elif choice == 2:
			choice = int(input("\nYou killed the goblin with a fire arrow. Enter 1 to bring back the goblin's gold to your village or enter 2 to bring back the goblin's magical mysterious potion to your village: "))

			if choice == 1:
				print("You brought back the goblin's gold to your village. The villagers are all very happy and have named you the new leader! The adventure has ended.\n")
			elif choice == 2:
				print("You brought back the goblin's potion to your village. Turns out it was just water but at least people are not living in fear of the goblin anymore. The adventure has ended.\n")
