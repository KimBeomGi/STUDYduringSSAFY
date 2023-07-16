const images = [
	"1_7월_디지털굿즈_PC_달력_3840x2160.png", "20201103벌똥별.jpg", "20211008가을준비.jpg", "20211024독서.jpg"
]

const chosenImage = images[Math.floor(Math.random() * images.length)]

console.log(chosenImage)

const bgImage = document.createElement("img")

bgImage.src = `img/${chosenImage}`

console.log(bgImage)


// document.body.appendChild(bgImage)
document.body.prepend(bgImage)