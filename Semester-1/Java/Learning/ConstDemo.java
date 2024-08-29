import java.util.*;
class LearnConst{
    int a,b;
    int r;
    LearnConst(){
        System.out.println("I am constructor!!!");
    }
    LearnConst(int a, int b){
        this.a = a;
        this.b = b;
    }
    void Addistion(){
        System.out.println(a+b);
    }
    LearnConst(int r){
        this.r = r;
    }
    void CircleArea(){
        double area = Math.PI * r * r;
        System.err.println(area);
    }
}


class ConstDemo{
    public static void main (String [] args){
        LearnConst t = new LearnConst();
        LearnConst t1 = new LearnConst(10,5);
        t1.Addistion();

        LearnConst t3 = new LearnConst(5);
        t3.CircleArea();

        System.out.println("This is ConstDemo class");
    }
}