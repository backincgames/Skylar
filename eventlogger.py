from colorama import Fore


def tagcolor(service: str):
  service = str.lower(service)
  if service == 'bot':
    color = Fore.BLUE
  elif service == 'sys':
    color = Fore.LIGHTBLUE_EX
  elif service == 'cogs' or service == 'warn':
    color = Fore.YELLOW
  elif service == 'ai' or service == 'ok':
    color = Fore.GREEN
  elif service == 'fail':
    color = Fore.RED
  else:
    color = Fore.WHITE
  return color
  
def printmsg(service: str,message: str,passfail: str = None):
  if passfail is not None:
    service = tagcolor(service)+'['+str.upper(service)+'] '
    if passfail == 'pass':
      passfail = 'ok'
    passfail = Fore.WHITE+'['+tagcolor(passfail)+str.upper(passfail)+Fore.WHITE+']: '
    if 'FAIL' in passfail:
      print(service+passfail+Fore.RED+message)
    else:
      print(service+passfail+message)
  else:
    service = tagcolor(service)+'['+str.upper(service)+']: '
    print(service+Fore.WHITE+message)
  return

# Depracated
def passfail(service,message,oktag):
  warn('sys','Old Logger API used')
  printmsg(service,message,oktag)

def warn(service,message):
  service = tagcolor(service)+'['+str.upper(service)+'] '
  warntag = Fore.WHITE+'['+tagcolor('warn')+str.upper('WARN')+Fore.WHITE+']: '
  print(service+warntag+message)