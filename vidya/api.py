import pyaiml as aiml, os, dataent

kernel = None

def get_kernel():
	global kernel
	if not kernel:
		kernel = aiml.Kernel()
		for basepath, folders, files in os.walk(dataent.get_app_path('vidya', 'aiml')):
			for filename in files:
				if filename.endswith('.aiml'):
					print 'learning {0}'.format(os.path.join(basepath, filename))
					kernel.learn(os.path.join(basepath, filename))
	return kernel

@dataent.whitelist(allow_guest=True)
def respond(q):
	k = get_kernel()
	return k.respond(q)