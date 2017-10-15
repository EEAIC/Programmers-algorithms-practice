import java.util.*;
public class ReverseInt {
    public int reverseInt(int n){
        String TmpString = String.valueOf(n);
        String[] TmpStringArray = TmpString.split("");
        List<Integer> TmpList = new ArrayList<Integer>();
        for (String i : TmpStringArray){
            TmpList.add(Integer.parseInt(i));
        }
        for(int i=0;i<TmpList.size();i++){
            for(int j=0;j<TmpList.size();j++){
                if (TmpList.get(i) > TmpList.get(j)){
                    int tmp = 0;
                    tmp = TmpList.get(i);
                    TmpList.set(i, TmpList.get(j));
                    TmpList.set(j, tmp);
                }
            }
        }
        int rst = 0;
        for(int i=0;i<TmpList.size();i++){
            rst += TmpList.get(i) * Math.pow (10 , (TmpList.size() - i - 1));
        }
        return rst;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        ReverseInt ri = new ReverseInt();
        System.out.println(ri.reverseInt(118372));
    }
}