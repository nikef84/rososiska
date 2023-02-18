#!/usr/bin/env python3

import time

def main():
	print(f"Hello ROS world!")
	for _ in range(5):
		current_time = time.localtime(time.time())
		print(f'{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}')
		time.sleep(5)
	
if __name__ == "__main__":
	main()
