import zlib
import os
import sys


def read_from_hex_offset(file, hex_offset: int) -> str:
	"""
	Fetch 3 bytes from file at the specified hexadecimal offset.
	:param file: The file object.
	:param hex_offset: The offset to the hexadecimal location, in decimal.
	"""
	
	filesize: int = os.path.getsize(file.name)
	
	if hex_offset > filesize:  # If the offset is greater than the filesize, loop back to the beginning over and over.
		timeslooping = hex_offset // filesize
		hex_offset -= timeslooping * filesize
	
	file.seek(hex_offset)
	return file.read(3).hex()
	
	
def main(pathtofile) -> str:
	"""
	Takes a file path and returns the canonical color of the file. (legally binding)
	:param pathtofile: A string representing the path to the file. (E.g. "C:/Users/username/Desktop/file.txt")
	:return: a string representing the canonical color of the file. (E.g. "64AAA5")
	"""

	filesize: int = os.path.getsize(pathtofile)

	# Pass the file object and the hex offset to the read_from_hex_offset function then print the result.
	with open(path, 'rb') as targetFile:
		crc32: int = zlib.crc32(targetFile.read())
		hexoffset: int = abs(filesize - crc32)
		
		hexcolor: str = read_from_hex_offset(targetFile, hexoffset).upper()
	
	print(f"Hex: {hexcolor}")  # Delete this line if you don't want to print the hex color.
	return hexcolor
		
		
if __name__ == "__main__":
	
	try:  # Get the path from the command line arguments.
		path = sys.argv[1]
	except IndexError:
		print("Usage: python main.py <path>")
		sys.exit(1)
	
	if '"' in path:
		path = path.replace('"', '')
		
	if '<' in path or '>' in path:
		path = path.replace('<', '').replace('>', '')
	
	if not os.path.exists(path):
		print("Path does not exist.")
		sys.exit(1)
	
	main(path)
