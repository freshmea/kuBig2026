// → HSV 변환
// → 노란색 테이프 threshold
// → morphology로 노이즈 제거
// → 테이프 contour 검출
// → approxPolyDP로 테이프 4점 검출
// → 노란색 테이프 기준 homography 생성
// → 종이 영역 threshold
// → 종이 contour / polygon 검출
// → 종이 contour를 homography로 변환
// → contourArea로 비율 넓이 계산
// 비정형의 노트의 넓이를 카메라로 계산하기