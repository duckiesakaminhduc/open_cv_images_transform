import cv2
import numpy as np


def contrast(path_img):
    filtersize = (3, 3);
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filtersize)
    input_img = cv2.imread(path_img)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    # phép toán hình thái học morphologyEx, xử lí ảnh nhị phân -> lấy biên, tô vùng...
    top_hat = cv2.morphologyEx(input_img, cv2.MORPH_TOPHAT, kernel, iterations=20)
    black_hat = cv2.morphologyEx(top_hat, cv2.MORPH_BLACKHAT, kernel, iterations=20)
    imgPlusTopHat = cv2.add(input_img, top_hat)
    imgSubtract = cv2.subtract(imgPlusTopHat, black_hat)
    cv2.imshow('original', input_img)
    # cv2.imshow('top_hat', top_hat)
    cv2.imshow('after_subContract', imgSubtract)
    cv2.waitKey(10000)
    return imgSubtract


# def gaussFilter(img):


import cv2
import numpy as np


def contrast(path_img):
    filtersize = (3, 3);
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filtersize)
    input_img = cv2.imread(path_img)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    # phép toán hình thái học morphologyEx, xử lí ảnh nhị phân -> lấy biên, tô vùng...
    top_hat = cv2.morphologyEx(input_img, cv2.MORPH_TOPHAT, kernel, iterations=20)
    black_hat = cv2.morphologyEx(top_hat, cv2.MORPH_BLACKHAT, kernel, iterations=20)
    imgPlusTopHat = cv2.add(input_img, top_hat)
    imgSubtract = cv2.subtract(imgPlusTopHat, black_hat)
    cv2.imshow('original', input_img)
    # cv2.imshow('top_hat', top_hat)
    cv2.imshow('after_subContract', imgSubtract)
    # cv2.waitKey(10000)
    return imgSubtract


def gaussFilter(path_img):
    img = contrast(path_img)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow('gaussFilter', img)
    # cv2.waitKey(10000)
    return img

# contrast('./data/img_2.png')

gaussFilter('./data/img_2.png')