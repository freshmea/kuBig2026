#include "colors.hpp"
#include <cmath>
#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

String folderPath = "/home/aa/kuBig2026/opencv_ex/data/";

int main()
{
    VideoCapture cap(0, CAP_V4L2);

    if (!cap.isOpened())
    {
        cerr << "카메라를 열 수 없습니다." << endl;
        return -1;
    }

    // 카메라 설정
    cap.set(CAP_PROP_FOURCC, VideoWriter::fourcc('M', 'J', 'P', 'G'));
    cap.set(CAP_PROP_FRAME_WIDTH, 640);
    cap.set(CAP_PROP_FRAME_HEIGHT, 480);
    cap.set(CAP_PROP_FPS, 30);

    int w = 640;
    int h = 480;
    double fps = 30.0;
    int fourcc = VideoWriter::fourcc('D', 'I', 'V', 'X');

    VideoWriter outVideo(folderPath + "happy_birthday_camera_effect.avi",
                         fourcc, fps, Size(w, h));

    if (!outVideo.isOpened())
    {
        cerr << "동영상 파일을 저장할 수 없습니다." << endl;
        return -1;
    }

    Mat frame;

    int roiSize = 200;
    int roiY = (h - roiSize) / 2;
    int moveX = 0;

    int t = 0;

    while (true)
    {
        cap >> frame;

        if (frame.empty())
        {
            cerr << "프레임을 읽을 수 없습니다." << endl;
            break;
        }

        resize(frame, frame, Size(w, h));
        flip(frame, frame, 1);

        // -----------------------------
        // 움직이는 반전 ROI 효과
        // -----------------------------
        Rect roiRect(moveX, roiY, roiSize, roiSize);
        Mat roi = frame(roiRect);

        bitwise_not(roi, roi);

        rectangle(frame, roiRect, Color::Red, 3, LINE_AA);

        drawMarker(frame,
                   Point(moveX + roiSize / 2, roiY + roiSize / 2),
                   Color::Yellow,
                   MARKER_STAR,
                   30,
                   2,
                   LINE_AA);

        // -----------------------------
        // 배경 반짝이 효과
        // -----------------------------
        for (int i = 0; i < 30; i++)
        {
            int x = (i * 83 + t * 4) % w;
            int y = (i * 47 + t * 3) % h;

            if ((i + t / 5) % 3 == 0)
            {
                drawMarker(frame,
                           Point(x, y),
                           Color::Yellow,
                           MARKER_STAR,
                           14,
                           1,
                           LINE_AA);
            }
            else if ((i + t / 5) % 3 == 1)
            {
                circle(frame,
                       Point(x, y),
                       4,
                       Color::Cyan,
                       FILLED,
                       LINE_AA);
            }
            else
            {
                rectangle(frame,
                          Rect(x, y, 7, 7),
                          Color::Magenta,
                          FILLED,
                          LINE_AA);
            }
        }

        // -----------------------------
        // 폭죽 효과 1
        // -----------------------------
        Point fire1(120, 90);
        int r1 = 20 + (t * 2) % 70;

        for (int i = 0; i < 12; i++)
        {
            double angle = CV_2PI * i / 12.0;

            Point p(
                fire1.x + (int)(cos(angle) * r1),
                fire1.y + (int)(sin(angle) * r1));

            line(frame, fire1, p, Color::Orange, 2, LINE_AA);
            drawMarker(frame, p, Color::Yellow, MARKER_STAR, 8, 1, LINE_AA);
        }

        // -----------------------------
        // 폭죽 효과 2
        // -----------------------------
        Point fire2(520, 100);
        int r2 = 15 + (t * 3) % 65;

        for (int i = 0; i < 14; i++)
        {
            double angle = CV_2PI * i / 14.0;

            Point p(
                fire2.x + (int)(cos(angle) * r2),
                fire2.y + (int)(sin(angle) * r2));

            line(frame, fire2, p, Color::Cyan, 2, LINE_AA);
            drawMarker(frame, p, Color::Red, MARKER_STAR, 8, 1, LINE_AA);
        }

        // -----------------------------
        // 케이크 받침
        // -----------------------------
        ellipse(frame,
                Point(320, 430),
                Size(190, 35),
                0,
                0,
                360,
                Color::White,
                FILLED,
                LINE_AA);

        ellipse(frame,
                Point(320, 430),
                Size(190, 35),
                0,
                0,
                360,
                Color::Blue,
                3,
                LINE_AA);

        // -----------------------------
        // 케이크 1층
        // Pink가 colors.hpp에 없으면 Scalar(203, 192, 255) 사용
        // RGB Pink = 255,192,203
        // OpenCV BGR = 203,192,255
        // -----------------------------
        rectangle(frame,
                  Rect(190, 330, 260, 90),
                  Scalar(203, 192, 255),
                  FILLED,
                  LINE_AA);

        rectangle(frame,
                  Rect(190, 330, 260, 90),
                  Color::White,
                  3,
                  LINE_AA);

        // 크림 장식
        for (int x = 205; x <= 435; x += 30)
        {
            circle(frame,
                   Point(x, 330),
                   14,
                   Color::White,
                   FILLED,
                   LINE_AA);
        }

        // 케이크 무늬
        for (int x = 210; x <= 410; x += 40)
        {
            line(frame,
                 Point(x, 350),
                 Point(x + 20, 400),
                 Color::Red,
                 2,
                 LINE_AA);

            line(frame,
                 Point(x + 20, 350),
                 Point(x, 400),
                 Color::Yellow,
                 2,
                 LINE_AA);
        }

        // -----------------------------
        // 케이크 2층
        // -----------------------------
        rectangle(frame,
                  Rect(240, 270, 160, 70),
                  Color::Orange,
                  FILLED,
                  LINE_AA);

        rectangle(frame,
                  Rect(240, 270, 160, 70),
                  Color::White,
                  3,
                  LINE_AA);

        for (int x = 255; x <= 385; x += 25)
        {
            circle(frame,
                   Point(x, 270),
                   12,
                   Color::White,
                   FILLED,
                   LINE_AA);
        }

        // -----------------------------
        // 초 + 불꽃
        // -----------------------------
        int flameMove = (t % 10 < 5) ? 0 : 5;

        for (int x = 260; x <= 380; x += 30)
        {
            rectangle(frame,
                      Rect(x, 220, 12, 50),
                      Color::Cyan,
                      FILLED,
                      LINE_AA);

            rectangle(frame,
                      Rect(x, 220, 12, 50),
                      Color::White,
                      1,
                      LINE_AA);

            line(frame,
                 Point(x, 230),
                 Point(x + 12, 240),
                 Color::Blue,
                 1,
                 LINE_AA);

            line(frame,
                 Point(x, 245),
                 Point(x + 12, 255),
                 Color::Blue,
                 1,
                 LINE_AA);

            ellipse(frame,
                    Point(x + 6, 210 - flameMove),
                    Size(8, 15),
                    0,
                    0,
                    360,
                    Color::Yellow,
                    FILLED,
                    LINE_AA);

            ellipse(frame,
                    Point(x + 6, 214 - flameMove),
                    Size(4, 8),
                    0,
                    0,
                    360,
                    Color::Red,
                    FILLED,
                    LINE_AA);
        }

        // -----------------------------
        // 떠오르는 풍선 효과
        // -----------------------------
        int balloonY = 460 - (t * 2 % 560);

        // 왼쪽 하트 풍선
        circle(frame,
               Point(70, balloonY),
               18,
               Color::Red,
               FILLED,
               LINE_AA);

        circle(frame,
               Point(95, balloonY),
               18,
               Color::Red,
               FILLED,
               LINE_AA);

        ellipse(frame,
                Point(82, balloonY + 18),
                Size(28, 35),
                0,
                0,
                360,
                Color::Red,
                FILLED,
                LINE_AA);

        line(frame,
             Point(82, balloonY + 50),
             Point(75, balloonY + 110),
             Color::White,
             1,
             LINE_AA);

        // 오른쪽 하트 풍선
        circle(frame,
               Point(545, balloonY + 60),
               18,
               Color::Cyan,
               FILLED,
               LINE_AA);

        circle(frame,
               Point(570, balloonY + 60),
               18,
               Color::Cyan,
               FILLED,
               LINE_AA);

        ellipse(frame,
                Point(557, balloonY + 78),
                Size(28, 35),
                0,
                0,
                360,
                Color::Cyan,
                FILLED,
                LINE_AA);

        line(frame,
             Point(557, balloonY + 110),
             Point(565, balloonY + 170),
             Color::White,
             1,
             LINE_AA);

        // -----------------------------
        // 축하 왕관 장식
        // -----------------------------
        line(frame, Point(270, 130), Point(290, 95), Color::Yellow, 3, LINE_AA);
        line(frame, Point(290, 95), Point(320, 130), Color::Yellow, 3, LINE_AA);
        line(frame, Point(320, 130), Point(350, 95), Color::Yellow, 3, LINE_AA);
        line(frame, Point(350, 95), Point(370, 130), Color::Yellow, 3, LINE_AA);
        line(frame, Point(270, 130), Point(370, 130), Color::Yellow, 3, LINE_AA);

        circle(frame, Point(290, 95), 6, Color::Red, FILLED, LINE_AA);
        circle(frame, Point(350, 95), 6, Color::Cyan, FILLED, LINE_AA);
        circle(frame, Point(320, 130), 6, Color::Magenta, FILLED, LINE_AA);

        // -----------------------------
        // 위로 올라가는 축하 화살표
        // -----------------------------
        int arrowY = 480 - (t * 4 % 300);

        arrowedLine(frame,
                    Point(35, arrowY + 50),
                    Point(35, arrowY),
                    Color::Yellow,
                    2,
                    LINE_AA);

        arrowedLine(frame,
                    Point(605, arrowY + 50),
                    Point(605, arrowY),
                    Color::Yellow,
                    2,
                    LINE_AA);

        // -----------------------------
        // 저장 및 출력
        // -----------------------------
        outVideo << frame;
        imshow("Happy Birthday Camera Effect", frame);

        if (waitKey(1000 / 30) == 27)
            break;

        moveX += 2;

        if (moveX > w - roiSize)
        {
            moveX = 0;
        }

        t++;
    }

    cap.release();
    outVideo.release();
    destroyAllWindows();

    return 0;
}