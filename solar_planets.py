import cv2

img = "solar-system.jpg"

cv2.imread("solar-system.jpg")
cv2.imshow("resultado",img)
cv2.waitKey(0)

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (120,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Venus",
            (140,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Terra",
            (160,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Marte",
            (180,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Jupiter",
            (200,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Saturno",
            (220,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Uranio",
            (240,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Netuno",
            (260,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )