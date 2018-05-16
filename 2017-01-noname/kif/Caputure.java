package kif;

import java.util.*;

/**
*持ち駒を管理するクラス
*/
public class Caputure {
    /** どの駒をどれだけ持っているかを格納する配列 */
    private int[] pieces={
        -1/*NU*/,0/*FU*/,0/*KY*/,0/*KE*/,0/*GI*/,0/*KI*/,0/*KA*/,0/*HI*/,
    };

    /** 持ち駒を追加する
    @param p 追加したい駒の種類
    @return 追加した駒のid 追加に失敗したら"0"
    */
    public int add(kif.Piece.Type p){
        //idが0(Type.NU),8(王将)またはそれ以外であれば失敗とする．
        //9-14は成り駒なので，普通の駒に変換してから追加する
        int id=p.getInt();

        if(id==0||id==8){
            //0(Type.NU),8(王将)
            return 0;
        }else if(id>=1&&id<=7){
            //普通の駒は変換しない
        }else if(id>=9&&id<=12){
            //成り駒（竜馬，竜王以外）
            //{9,10,11,12}->{1,2,3,4}に変換
            id-=8;
        }else if(id>=13&&id<=14){
            //竜王．竜馬
            //{13,14}->{6,7}に変換
            id-=7;
        }
        this.pieces[id]++;
        return id;
    }
    /** 持ち駒を追加する
    @param p 追加したい駒のid
    @return 追加した駒のid 追加に失敗したら"0"
    */
    public int add(int p){
        return add(kif.Piece.getType(p));
    }

    /** 持ち駒を使用する
    @param p 使用したい駒の種類
    @return 使用した駒のid 使用に失敗したら"0"
    */
    public int use(kif.Piece.Type p){
        int id=p.getInt();
        //持っている駒であれば使用（減らす）
        if((id>=1&&id<=7)&&this.pieces[id]>0){
            this.pieces[id]--;
            return id;
        }
        return 0;
    }

    /** 持ち駒を使用する
    @param p 使用したい駒
    @return 使用した駒のid 使用に失敗したら"0"
    */
    public int use(kif.Piece p){
        return use(p.getPieceType());
    }

    /** 持ち駒を使用する
    @param p 使用したい駒のid
    @return 使用した駒のid 使用に失敗したら"0"
    */
    public int use(int p){
        return use(kif.Piece.getType(p));
    }

    /** 持ち駒を確認する
    *@return どの持ち駒がどれだけあるか
    */
    public int[] getCapture(){
        return this.pieces;
    }

    /** 持ち駒を確認する
    *@param i 駒のid
    *@return どの持ち駒がどれだけあるか
    */
    public int getCapture(int i){
        return this.pieces[i];
    }

}
