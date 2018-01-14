function alpha_string46(s){
  var result;
  if ( 4 == s.length || 6 == s.length){
  	result = parseInt(s); 
  }
  // 함수를 완성하세요
	if (typeof(result) == "number"){
  	return true;
  }
  else	{
  	return false;
  }
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( alpha_string46("a234") );