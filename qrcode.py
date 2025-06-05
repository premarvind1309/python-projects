import pyqrcode
import png
link ="https://www.linkedin.com/in/prem-aravind-papolu-802904230/"
qr = pyqrcode.create(link)
qr.png("myqr.png",scale=8)
