package kif;

/**
*駒の列挙型クラス
*/
public class Piece {
    /** 駒の種類 */
    public static enum Type {
        /** null駒 */
        NU("","",0),
        /** 歩兵 */
        FU("FU","歩兵",1),
        /** 香車 */
        KY("KY","香車",2),
        /** 桂馬 */
        KE("KE","桂馬",3),
        /** 銀将 */
        GI("GI","銀将",4),
        /** 金将 */
        KI("KI","金将",5),
        /** 角行 */
        KA("KA","角行",6),
        /** 飛車 */
        HI("HI","飛車",7),
        /** 王将 */
        OU("OU","王将",8),
        /** と金 */
        TO("TO","と金",9),
        /** 成香 */
        NY("NY","成香",10),
        /** 成桂 */
        NK("NK","成桂",11),
        /** 成銀 */
        NG("NG","成銀",12),
        /** 竜馬 */
        UM("UM","竜馬",13),
        /** 竜王 */
        RY("RY","竜王",14);

        /** テキスト（CSA） */
        private final String text;
        /** テキスト (日本語) */
        private final String text_ja;
        /** 識別用番号 */
        private final int id;

        private Type(final String text,final String text_ja , final int id) {
           this.text = text;
           this.text_ja = text_ja;
           this.id = id;
        }

        /**CSA形式のテキストを取得
        *@return CSA形式のテキスト
        */
        public String getString() {
            return this.text;
        }

        /**日本語形式のテキストを取得
        *@return 日本語形式のテキスト
        */
        public String getString_ja() {
            return this.text_ja;
        }

        /**駒idを取得
        *@return 駒のid
        */
        public int getInt() {
            return this.id;
        }
    }

    /** 先手か後手か空白の情報*/
    public static enum Turn {
        /** 空白 */
        NONE(0),
        /** 先手 */
        SENTE(1),
        /** 後手 */
        GOTE(-1);

        /** 識別用の数値 */
        private final int num;

        /** コンストラクタ */
        private Turn(final int n) {
           this.num = n;
        }

        /** 識別用の数値を取得
        *@return 識別用の数値
        */
        public int getInt() {
            return this.num;
        }
    }

    /** 駒の種類 */
    private Type type;
    /** 先手か後手か空白かの情報 (-1,0,+1)*/
    private Turn turn;

    /**コンストラクタ
    * @param ty 駒の種類
    * @param tr 先手か後手か
    */
    public Piece(Type ty, Turn tr){
        this.type=ty;
        this.turn=tr;
    }

    /**駒の種類を取得
    * @return 駒の種類
    */
    public Type getPieceType(){
        return this.type;
    }

    /**駒のidを取得
    * @return 駒のid
    */
    public int getPieceId(){
        return ((this.isSente())?(1):(-1))*this.type.getInt();
    }

    /**先手か否かを取得
    * @return 先手か否か
    */
    public boolean isSente(){
        return (this.turn.getInt()==Turn.SENTE.getInt());
    }

    /**駒の文字列を駒の向き込みで取得
    * @return "[先手+:後手-][駒の文字列]"
    */
    public String getPieceString(){
        String s = String.format("%s%s", this.isSente()?"+":"-", this.type.getString());
        if(this.type == Type.NU){
            s=" * ";
        }
        return s;
    }

    /**駒の日本語文字列を駒の向き込みで取得
    * @return "[先手+:後手-][駒の文字列]"
    */
    public String getPieceString_ja(){
        String s = String.format("%s%s", this.isSente() ? "+" : "-", this.type.getString_ja());
        if(this.type == Type.NU){
            s=" * ";
        }
        return s;
    }

    /** 駒を成らせる
    * @return どの駒になったか．成るのに失敗したら0
    */
    public int promote(){
        switch (this.type) {
        case FU:
            this.type = kif.Piece.Type.TO;
            break;
        case KY:
            this.type = kif.Piece.Type.NY;
            break;
        case KE:
            this.type = kif.Piece.Type.NK;
            break;
        case GI:
            this.type = kif.Piece.Type.NG;
            break;
        case KA:
            this.type = kif.Piece.Type.UM;
            break;
        case HI:
            this.type = kif.Piece.Type.RY;
            break;
        default:
            //駒がNU,OUかすでに成り駒
            return 0;
        }
        return this.getPieceId();
    }

    /** idから求める駒を持ってくる．
    * 見つからなかったらnull駒が帰ってきます
    * @param id 駒の識別番号
    * @return idに対応した駒
    */
    public static Type getType(final int id) {
        Type[] types = Type.values();
        for (Type type : types) {
            if (type.getInt() == Math.abs(id)) {
                return type;
            }
        }
        return Type.NU;
    }

    /** テキストから求める駒を持ってくる．
    * 見つからなかったらnull駒が帰ってきます
    * @param text 駒のテキスト(CSAまたは日本語)
    * @return テキストに対応した駒
    */
    public static Type getType(final String text) {
        Type[] types = Type.values();
        for (Type type : types) {
            if (type.getString().equals(text) || type.getString_ja().equals(text)) {
                return type;
            }
        }
        return Type.NU;
    }

    /** 数値から先手か後手か空白かの情報に変換する
    * @return 先手か後手か空白かの情報
    */
    public static Turn getTurn(final int num) {
        if(num>0){
            return Turn.SENTE;
        }else if(num<0){
            return Turn.GOTE;
        }
        return Turn.NONE;
    }
}
