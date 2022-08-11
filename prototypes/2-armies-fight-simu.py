from datetime import datetime
from tkinter import W
from ArmyFight import Army
from logging import Logger, INFO, FileHandler, StreamHandler

LOGGER: Logger = Logger("2ARMIES-SIMU", INFO)
file_handler = FileHandler("nemesys.log")
file_handler.setLevel(INFO)

stream_handler = StreamHandler()
stream_handler.setLevel(INFO)

LOGGER.addHandler(stream_handler)
LOGGER.addHandler(file_handler)

def start_battle(warriors_count: int, enemies_count: int, simultaneous_fights: int = 0):
    shadows_army = Army("Shadows", warriors_count)
    undead_army = Army("Undeads", enemies_count)

    start_timestamp_fight = datetime.now()
    LOGGER.info("{} - The combat between {} (x{}) and {} (x{}) is starting...".format(datetime.now(), shadows_army.name, warriors_count, undead_army.name, enemies_count))
    shadows_army.attack(target_army=undead_army, simultaneous_fights=simultaneous_fights)
    undead_army.attack(target_army=shadows_army, simultaneous_fights=simultaneous_fights)
    
    while (shadows_army.is_fighting() and undead_army.is_fighting()):
        continue

    stop_timestamp_fight = datetime.now()
    duration_date = (stop_timestamp_fight-start_timestamp_fight)
    days = duration_date.days
    hours = int((duration_date.seconds/60)/60)
    minutes = int(duration_date.seconds/60)
    seconds = duration_date.seconds % 60
    millis = duration_date.microseconds % 1000
    LOGGER.info("{} - The combat between {} and {} ({}x{}) lasted {} days {} hours {} minutes {} seconds {} milliseconds.".format(datetime.now(), shadows_army.name, undead_army.name, warriors_count, enemies_count, days, hours, minutes, seconds, millis))

def main():
    # start_battle(1, 1)
    # start_battle(2, 2)
    # start_battle(2, 5)
    # start_battle(5, 5)
    # start_battle(10, 10)
    # start_battle(50, 10)
    # start_battle(50, 50)
    total_warriors: int = 50
    total_undeads: int = 50
    threads_pool_size: int = 1
    total_tests: int = 1
    
    threads_pool_size: int = 0
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)

    threads_pool_size: int = 1
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)

    threads_pool_size: int = 2
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)

    threads_pool_size: int = 5
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)

    threads_pool_size: int = 10
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)

    threads_pool_size: int = 15
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)
        
    threads_pool_size: int = 20
    LOGGER.info("Thread Pool Size: {}".format(threads_pool_size))
    for _ in range(total_tests):
        start_battle(total_warriors, total_undeads, threads_pool_size)

    # start_battle(500, 100)
    # start_battle(1000, 1000)

if (__name__ == "__main__"):
    main()