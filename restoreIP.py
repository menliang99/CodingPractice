def RestoreIPAddress(s):

	def dfs(s, sub, ips, ip):
		if sub == 4:
			if s == '':
				print ip
				ips.append(ip[1:])
			return
		for i in range(1, 4):
			if i <= len(s):
				if int(s[:i]) <= 255:
					dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
				if s[0] == '0':
					break
	
	ips = []
	dfs(s, 0, ips, '')
	return ips

s = "101199023"
print RestoreIPAddress(s)
