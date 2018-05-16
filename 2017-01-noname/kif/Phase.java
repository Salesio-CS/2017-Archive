package kif;


/**
* 手番を格納する用のクラス
*/
public class Phase {
    /** 移動前の駒の位置
    * 駒台から打ったときは0とする
    */
    private kif.Position from;
    /** 移動後の駒の位置 */
    private kif.Position to;
    /** 移動した駒の種類 */
    private kif.Piece.Type type;
    /** 移動した駒 */
    private kif.Piece piece;
    /** かかった時間 */
    private int times;

    /** コンストラクタ
    * @param b 移動前の駒の位置
    * @param a 移動後の駒の位置
    * @param p 移動した駒の種類
    * @param t かかった時間
    */
    public Phase(kif.Position b,kif.Position a,kif.Piece p,int t){
        this.from=b;
        this.to=a;
        this.piece=p;
        this.times=t;
    }

    /** 手番用の文字列(CSA形式)を返す関数
    *@return "[先手:+,後手:-][移動前の駒の位置][移動後の駒の位置][駒の種類]"
    */
    public String getString(){
        String s=(this.isSente())?("+"):("-");
        return String.format("%s%d%d%d%d%s", s, this.from.getX(), this.from.getY(), this.to.getX(), this.to.getY(), this.piece.getPieceType().getString());
    }

    /**移動前の座標を取得する（旧名）
    *@return 移動前の座標クラス
    */
    public kif.Position getBefore(){
        return this.from;
    }

    /**移動後の座標を取得する（旧名）
    *@return 移動後の座標クラス
    */
    public kif.Position getAfter(){
        return this.to;
    }

    /**移動前の座標を取得する
    *@return 移動前の座標クラス
    */
    public kif.Position getFromPosition(){
        return this.from;
    }

    /**移動後の座標を取得する
    *@return 移動後の座標クラス
    */
    public kif.Position getToPosition(){
        return this.to;
    }

    /** 移動する駒を取得する
    * @return 移動する駒
    */
    public kif.Piece getPiece(){
        return this.piece;
    }

    /** 移動する駒の種類を取得する
    * @return 移動する駒の種類
    */
    public kif.Piece.Type getPieceType(){
        return this.piece.getPieceType();
    }

    /** 先手か否かを取得
    * @return 先手番であればtrue
    */
    public boolean isSente(){
        return this.piece.isSente();
    }

    /**駒が成れるか否かを取得
    *@return 成れるのであれば"true",そうでなければ"false"
    */
    public boolean canPromote(){
        if( this.piece.getPieceType() == kif.Piece.Type.NU || this.piece.getPieceType() == kif.Piece.Type.KI || this.piece.getPieceType() == kif.Piece.Type.OU ){
            //NU,KI,OUは成れない
            return false;
        }
        //移動前と後どの行にいるか
        int r1 = this.getFromPosition().getY();
        int r2 = this.getToPosition().getY();
        //成れる範囲
        int y1,y2;
        if(this.isSente()){
            //先手:上から3行
            y1 = 1;
            y2 = 3;
        }else{
            //後手:下から3行
            y1 = 6;
            y2 = 9;
        }

        //駒打の時は不可
        if( r1 == 0 ){
            return false;
        }

        //移動が成れる範囲にいれば可
        if(( y1 <= r1 && r1 <= y2 )||( y1 <= r2 && r2 <= y2 )){
            return true;
        }
        return false;
    }

    /** 駒を成らせる */
    public void setPromote(){
        this.piece.promote();
    }
}
