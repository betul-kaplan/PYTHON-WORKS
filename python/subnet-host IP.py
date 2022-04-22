The network address of 172.16.0.0/19 provides how many subnets and host?

def subnets(ip) :
  ip = ip.split("/")
  cidr = int(ip[1])
  ip_list = list(map(int,ip[0].split(".")))
  octet = cidr // 8
  bit = cidr % 8
  subnet = 2**bit
  host = (2**(32-cidr)) - 2
  return {"Subnets" : subnet, "Hosts" : host}

ip = "172.16.0.0/19"

print(subnets(ip))