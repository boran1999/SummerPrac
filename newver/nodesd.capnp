@0x9c40586b883c8604;

struct Node {
	id @0 :UInt32;
	name @1 : Text;
	value : union {
		none @2 : Void;
		num @3 : UInt32;
		fnum @4 : Float32;
		text @5 : Text;
		arr @6 : NDArray;
	}
	nodes @7 : List(Node); 
}


struct NDArray {
	shape @0 :List(UInt32);
	dtype @1 :DType;
	data @2 :Data;
	enum DType {
		bool @0;
		uint8 @1;
		uint16 @2;
		uint32 @3;
		uint64 @4;
		int8 @5;
		int16 @6;
		int32 @7;
		int64 @8;
		float32 @9;
		float64 @10;
		float128 @11;
	}
}
struct NestedList {
	list @0 :List(List(Int32));
}

