

# Forma de coletar informações sobre arquivos em um local do sistema

from os import scandir

this_path = 'C:\\Users\\lucasf\\Downloads\\youtube\\dbz'
target = tuple(scandir(this_path))

print(target)

print([1], target[0].inode())
print([2], target[0].is_dir())
print([3], target[0].is_file())
print([4], target[0].is_symlink())
print([5], target[0].name)
print([6], target[0].path)
print([7], target[0].stat())

print(dir(target[0]))
