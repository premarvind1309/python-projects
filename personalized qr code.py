import segno
#we will use reqd modules from segno
from segno import helpers
qr = helpers.make_mecard(name="prem",email="prem@gmaiil.com",phone = "+918519857307",url="www.linkedin.com/in/prem-aravind-papolu-802904230/")
qr.save("mycard.png",scale=10)
