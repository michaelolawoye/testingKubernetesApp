import os

container_name= os.getenv("IMAGE_NAME", "default")

print(f"This is a container made from image {container_name}")