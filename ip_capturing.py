import re
import ipaddress

class ip_log_analysis:
	''' a class with three methods which captures, 
	displays and copies the ip addresses'''

	def ip_capture(self, logfile):
		'''captures the ip addresses from an input file'''
		self.captured = set()
		with open(logfile) as file:
			for text in file:
				self.regex = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
				for line in self.regex:
					try:
						ipaddress.ip_address(line)
						self.captured.add(line)
					except ValueError:
						pass			
	def ip_display(self):
		'''displays the ip addresses captured from a file'''
		for ip in self.captured:
			print(ip)					


	def ip_copy(self, targetfile):
		'''copies the captured ip addresses to an input file'''
		with open(targetfile, "w") as f:
			for ip in self.captured:
				f.write(f"{ip}\n")



test = ip_log_analysis()
test.ip_capture("sample_strings.txt")
test.ip_display()
test.ip_copy("empty.txt")