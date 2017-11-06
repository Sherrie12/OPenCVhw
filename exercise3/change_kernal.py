
import cv2
import numpy as np

def Add_gaussian_Noise(src,mean,sigma):
	image = src.copy()
	cv2.randn(image,mean,sigma)
	cv2.add(src,image,image)
	return image

def SaltAndPepper(src,pa,pb):
	NoiseImg = src
	NoiseNum1 = int(pa*src.shape[0]*src.shape[1])
	for i in range(NoiseNum1):
		randX=np.random.random_integers(0,src.shape[0]-1)
		randY=np.random.random_integers(0,src.shape[1]-1)
		NoiseImg[randX,randY]=0
	NoiseNum2 = int(pb*src.shape[0]*src.shape[1])
	for i in range(NoiseNum2):
		randX=np.random.random_integers(0,src.shape[0]-1)
		randY=np.random.random_integers(0,src.shape[1]-1)
		NoiseImg[randX,randY]=255         
	return NoiseImg 

def main():
	src = cv2.imread("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/Test_images/Lenna.png")
	gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
	
# Gaussain noise
	mean,sigma = 0,25
	gaussian_noise = Add_gaussian_Noise(gray,mean,sigma)
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_GN_Gaussian_noise.png", gaussian_noise)

	# Box filter
	noise_dst = gaussian_noise.copy()
	box_filter = cv2.blur(noise_dst,(5,5))
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_GN_Box_filter.png", box_filter)

	# Gaussain filter
	noise_dst1 = gaussian_noise.copy()
	gaussian_filter = cv2.GaussianBlur(noise_dst1,(5,5),1.5)
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_GN_Gaussian_filter.png", gaussian_filter)

	# Median filter
	noise_dst2 = gaussian_noise.copy()
	median_filter = cv2.medianBlur(noise_dst2,3)
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_GN_Median_filter.png", median_filter)

# Sault and Pepper noise
	pa,pb = 0.01,0.01
	sp_noise = SaltAndPepper(gray,pa,pb)
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_SP_Gaussian_noise.png", sp_noise)

	# Box filter
	noise_dst = sp_noise.copy()
	box_filter = cv2.blur(noise_dst,(5,5))
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_SP_Box_filter.png", box_filter)

	# Gaussain filter
	noise_dst1 = sp_noise.copy()
	gaussian_filter = cv2.GaussianBlur(noise_dst1,(5,5),1.5)
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_SP_Gaussian_filter.png", gaussian_filter)

	# Median filter
	noise_dst2 = sp_noise.copy()
	median_filter = cv2.medianBlur(noise_dst2,3)
	cv2.imwrite("/Users/wangchunxi/BU/courses/EC601/OpenCV_homework/hw/exercise3/kernal_change/5*5_SP_Median_filter.png", median_filter)



if __name__=="__main__":
	main()

