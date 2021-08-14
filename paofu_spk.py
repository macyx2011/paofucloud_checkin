import pyttsx3


def paofuspk(requests_status:int,log_status:bool,check_status:bool,check_data:int,position_status:bool):
	if:

	else:
		if requests_status != 200:
			requests_problem = ['It\'s requests problem.','Requests false, sir']
			a = random()
		elif position_status != False:
			a = "I can send post, but the website composition has changed."
		return ("Sir. I can't signed from the sign site."+a)

if __name__ == "__main__":
	spk = pyttsx3.init()
	spk.say(paofuspk(200,True,True,300,True))
	spk.runAndWait()