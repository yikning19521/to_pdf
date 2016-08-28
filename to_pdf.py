import os
import shutil
import sys

def stripEndingSlash(path):
	if (path[-1] == '/'):
		return path[:-1]
	return path


if __name__ == "__main__":
	args = sys.argv[1:]
	argc = len(args)
	if (argc != 2):
		raise Exception("Need two arguments; you've provided " + str(argc))
	[srcDir, dstDir] = args

	if ((srcDir == dstDir) or (os.path.abspath(srcDir) == os.path.abspath(dstDir))):
		errorString = 'Need to give two different directories. {0} is the same as {1}'.format(srcDir, dstDir)
		raise Exception(errorString)

	srcDir = stripEndingSlash(srcDir)
	dstDir = stripEndingSlash(dstDir)

	files = os.listdir(srcDir)

	for file in files:
		shutil.copyfile(srcDir + '/' + file, dstDir + '/' + file + '.pdf')



		


