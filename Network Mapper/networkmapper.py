from email.policy import default
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-H", "--HOST", action="store", type="string", dest="hostname")
parser.add_option("-p", "--port", action="store", type="string", dest="portNumber")
parser.add_option("-h", "--help", action="store_true", dest="displayHelp", default=False) #TODO: create proper help menu

(options, args) = parser.parse_args()

print(options)
print(args)
