/*Tau sayısı, bir sayının tam bölenlerinin tam bölünebilinebilen sayılara denir.
 * Örnek :
 *24 tam bölenleri(1,2,3,4,6,12,24"8 adet") 24mod8=0 olduğu için 24 bir Tau sayısıdır.

 1000 e kadar kaç tane Tau sayısı vardır*/
#include <stdio.h>
int bolen;
int sayac;
sayac=0;

int bolum_kont(int sayi){
    bolen=0;
    for(int j=1;j<=sayi;j++){
        if(sayi%j==0){
            bolen=bolen+1;
        }
     }
    if (sayi%bolen==0){
        sayac++;
    }
}

int main(){
    for(int i=1;i<=1000;i++){
        bolum_kont(i);
    }
    printf("%d\n",sayac);
}

