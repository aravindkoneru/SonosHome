import soco
import random
import Queue

speakers = soco.discover();
bedroom = None

for speaker in speakers:
	if speaker.player_name == "Bedroom":
		bedroom = speaker
		break;

assert(bedroom != None), "Could not find Bedroom Sonos!"

playback = bedroom.get_current_transport_info()['current_transport_state']

if playback == 'PLAYING':
	bedroom.volume = 0
	bedroom.pause()
	bedroom.status_light = False

old_queue = bedroom.get_queue()
new_array = []

for x in range(0, len(old_queue)):
	new_array.append(old_queue.pop())
	bedroom.remove_from_queue(x)

random.shuffle(new_array)

for x in range(0, len(new_array)):
	bedroom.add_to_queue(new_array[x])

playback = bedroom.get_current_transport_info()['current_transport_state']

if playback == 'PAUSED_PLAYBACK' or playback == 'STOPPED':
	bedroom.volume = 10
	bedroom.play()
	bedroom.status_light = True

