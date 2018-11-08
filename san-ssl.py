import subprocess
import argparse
import sys

def get_san(domain):
  cmd='echo|openssl s_client -connect '
  domainl=domain+':443'
  half=' 2>/dev/null | openssl x509 -noout -text | grep "Subject Alternative Name" -A2 | grep -Eo "DNS:[a-zA-Z 0-9.*-]*" |  sed "s/DNS://g"'
  #cmd = 'ls|grep abc'
  cmd=cmd+domainl+half
  process = subprocess.Popen(cmd, shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
  process.wait()
  stdout, stderr = process.communicate()
  print stdout,stderr

def check_arg(args=None):
  parser = argparse.ArgumentParser(description='Subject Alternative name from SSL certificate of Live site')
  parser.add_argument('-d','--domain',help='domain format - google.com', required='True')
  results = parser.parse_args(args)
  return results.domain

if __name__ == '__main__':
  d = check_arg(sys.argv[1:])
  print '-'*50
  print '> '+d
  get_san(d.strip())
  print '-'*50
