import os

base_dir = "dataset"

if not os.path.exists(base_dir):
    raise FileNotFoundError(f"O diretório '{base_dir}' não foi encontrado.")

files = sorted(os.listdir(base_dir))

counter = 1
for file in files:
    old_path = os.path.join(base_dir, file)

    if not os.path.isfile(old_path):
        continue

    new_name = f"{counter}.jpg"
    new_path = os.path.join(base_dir, new_name)

    os.rename(old_path, new_path)
    counter += 1
