import os
print("Hello from the container!")

container_name= os.getenv("IMAGE_VERSION", "default")

print(f"This is a container made from image {container_name}")