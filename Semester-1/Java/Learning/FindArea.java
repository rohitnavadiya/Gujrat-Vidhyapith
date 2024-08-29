import java.util.*;
abstract class Area{
    abstract void area();
}

class CircleArea extends Area{
    double r=10;
    void area(){
        // System.out.println(Math.PI*r*r);
        System.out.println(Math.PI*r*r);
    }
}

class RectArea extends Area{
    double l = 10;
    double w = 20;
    void area(){
        System.err.println(l*w);
    }
}

class FindArea{
    public static void main(String args[]){
        // System.out.println("Hello java");
        Area a1 = new CircleArea();
        a1.area();
    }
}