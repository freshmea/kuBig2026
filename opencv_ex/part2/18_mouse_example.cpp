// 마우스를 따라다니는 사각형 박스를 만드세요.
// 마우스 오른쪽 버튼을 누르면 사각형 박스의 색깔이 랜덤으로 변경되도록 하세요.
// 왼쪽 버튼을 누르고 움직이면 선(사각형 박스의 색깔과 같은) 선이 그어지도록 하세요.
// 휠 버튼을 누르면(스포이드 기능) 마우스 위치의 픽셀 정보로 사각형 박스의 색깔을 변화 시키세요.

#include "colors.hpp"
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

struct MouseData
{
    Mat *img;
    Point mousePt;
    Point ptOld;
    Scalar boxColor;
    bool pushed;
    int boxSize;
};

void on_mouse(int event, int x, int y, int flags, void *data);

int main()
{
    const String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";
    Mat img = imread(folderPath + "lenna.bmp");

    if (img.empty())
    {
        cerr << "이미지를 불러올 수 없습니다." << endl;
        return -1;
    }

    MouseData mouseData;
    mouseData.img = &img;
    mouseData.mousePt = Point(0, 0);
    mouseData.ptOld = Point(0, 0);
    mouseData.boxColor = Color::Red;
    mouseData.pushed = false;
    mouseData.boxSize = 60;

    namedWindow("img");
    setMouseCallback("img", on_mouse, (void *)&mouseData);

    while (true)
    {
        Mat display = img.clone();

        Rect boxRect(
            mouseData.mousePt.x - mouseData.boxSize / 2,
            mouseData.mousePt.y - mouseData.boxSize / 2,
            mouseData.boxSize,
            mouseData.boxSize);

        boxRect &= Rect(0, 0, display.cols, display.rows);

        rectangle(display, boxRect, mouseData.boxColor, 2, LINE_AA);

        imshow("img", display);

        if (waitKey(30) == 27)
            break;
    }

    destroyAllWindows();

    return 0;
}

void on_mouse(int event, int x, int y, int flags, void *data)
{
    MouseData *mouseData = (MouseData *)data;
    Mat *img = mouseData->img;

    mouseData->mousePt = Point(x, y);

    static RNG rng((uint64)getTickCount());

    switch (event)
    {
    case EVENT_LBUTTONDOWN:
        mouseData->pushed = true;
        mouseData->ptOld = Point(x, y);
        break;

    case EVENT_LBUTTONUP:
        mouseData->pushed = false;
        break;

    case EVENT_MOUSEMOVE:
        if (mouseData->pushed)
        {
            line(
                *img,
                mouseData->ptOld,
                Point(x, y),
                mouseData->boxColor,
                2,
                LINE_AA);

            mouseData->ptOld = Point(x, y);
        }
        break;

    case EVENT_RBUTTONDOWN:
        mouseData->boxColor = Scalar(
            rng.uniform(0, 256),
            rng.uniform(0, 256),
            rng.uniform(0, 256));

        cout << "랜덤 색상 BGR: "
             << mouseData->boxColor[0] << ", "
             << mouseData->boxColor[1] << ", "
             << mouseData->boxColor[2] << endl;
        break;

    case EVENT_MBUTTONDOWN:
        if (x >= 0 && x < img->cols && y >= 0 && y < img->rows)
        {
            Vec3b pixel = img->at<Vec3b>(y, x);

            mouseData->boxColor = Scalar(
                pixel[0],
                pixel[1],
                pixel[2]);

            cout << "스포이드 색상 BGR: "
                 << (int)pixel[0] << ", "
                 << (int)pixel[1] << ", "
                 << (int)pixel[2] << endl;
        }
        break;
    }
}