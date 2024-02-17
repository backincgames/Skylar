from colorama import Fore


def tagcolor(service: str):
  service = str.lower(service)
  if service == 'bot':
    color = Fore.BLUE
  elif service == 'cogs' or service == 'warn':
    color = Fore.YELLOW
  elif service == 'ai' or service == 'ok':
    color = Fore.GREEN
  elif service == 'fail':
    color = Fore.RED
  else:
    color = Fore.WHITE
  return color
  
def printmsg(service: str,message: str):
  service = tagcolor(service)+'['+str.upper(service)+']: '
  print(service+Fore.WHITE+message)
  return

def passfail(service,message,oktag):
  service = tagcolor(service)+'['+str.upper(service)+'] '
  if oktag == 'pass':
    oktag = 'ok'
  oktag = Fore.WHITE+'['+tagcolor(oktag)+str.upper(oktag)+Fore.WHITE+']: '
  if 'FAIL' in oktag:
    print(service+oktag+Fore.RED+message)
  else:
    print(service+oktag+message)

def warn(service,message):
  service = tagcolor(service)+'['+str.upper(service)+'] '
  warntag = Fore.WHITE+'['+tagcolor('warn')+str.upper('WARN')+Fore.WHITE+']: '
  print(service+warntag+message)