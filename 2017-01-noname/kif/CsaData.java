package kif;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.time.*;
import java.util.*;

/**
*情報入力してcsaファイルに書き込むクラス
*/
public class CsaData {
    /** 先手 */
    private String sente;
    /** 後手 */
    private String gote;
    /** 場所 */
    private String place;
    /** 開始の時刻 */
    private LocalDateTime start;
    /** 終了の時刻 */
    private LocalDateTime end;
    /** 棋譜のリスト */
    private ArrayList<kif.Phase> phaseLog;

    /** コンストラクタ
    * @param s 先手の名前
    * @param g 後手の名前
    * @param p 対局場所
    */
    public CsaData(String s,String g,String p){
        this.sente = s;
        this.gote = g;
        this.place = p;
        this.start = LocalDateTime.now();
        this.phaseLog = new ArrayList<>();
    }

    /** 手番を追加する
    * @param p 移動する手番
    */
    public void addPhaseLog(kif.Phase p){
        this.phaseLog.add(p);
    }

    /** 手番のログ（棋譜）を取得
    * @return 手番型のリスト
    */
    public ArrayList<kif.Phase> getPhaseLog(){
        return this.phaseLog;
    }

    /**CSA型の文字列を取得
    *@return csa型の文字列
    */
    public String getCSAString(){
        String s="v2.2\n";
        //対局情報
        // s+=String.format("N+%s\n",this.sente);
        // s+=String.format("N-%s\n",this.gote);
        // s+=String.format("$SITE:%s\n",this.place);
        //初期局面取得
        s+=new kif.Board().getBoardString();
        s+="+\n";
        //手番
        for (kif.Phase p : this.phaseLog) {
            s+= p.getString() + ",T1\n";
        }
        //終わり
        s+="%TORYO,T1";
        return s;
    }



}
