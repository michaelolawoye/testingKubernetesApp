print("Hello from the container!")

with open("read.txt", "r") as f:
	s = f.read()
	print(f"File contents is: {s}")

