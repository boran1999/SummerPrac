@0x9c40586b883c8604;

const qux :UInt32 = 123;

struct Sundata {
  id @0 :UInt32;
  name @1: Text;
  data @2 :Array;
  image @3 : Array;
  timestamp @4 : Text;
  number @5 : UInt32;
  type @6 : Text;
  flatField @7 : Array;
  darkFrame @8 : Array;
  reference @9 : UInt32;
  signal1 @10 : Array;
  signal2 @11 : Array;
  metadata @12 : Meta;
  spectr @13 : Text;
  timeCoord @14 : TCoord;
}

struct Array {
  values @0 : Text;
  size @1 : Text;
  type @2 : Text;
}

struct Meta{
  ipol @0 : UInt32;
  pixelSize @1 : Float32;
  units @2 : Text;
  cameraSettingsTree @3 : CMT;
}

struct TCoord{
  coordLat @0 : Array;
  coordLon @1 : Array;
  coordX @2 : Array;
  coordY @3 : Array;
  epochTime @4 : Array;
  isoTime @5 : Text;
}

struct CMT{
  image @0 : ImDat;
  timings @1 : Time;
  buffer @2 : Buff;
  device @3 : Devme;
}

struct ImDat{
  dataType @0 : UInt32;
  binX @1 : UInt32;
  binY @2 : UInt32;
  dataTypeBytes @3 : UInt32;
  fileToWrite @4 : Text;
  imageX @5 : UInt32;
  imageY @6 : UInt32;
  roi @7 : Roi;
}

struct Roi{
  roi1 @0 : Text;
  totalRoi @1 : UInt32;
}

struct Time{
  freeq @0 : UInt32;
  exTime @1 : UInt32;
  exUnits @2 : Text;
  syncType @3 : UInt32;
}

struct Buff{
  buffControlTimeout @0 : UInt32;
  buffElemSize @1 : UInt32;
  buffFpe @2 : UInt32;
  buffFrameSize @3 : UInt32;
  buffLen @4 : UInt32;
  buffModulStates @5 : UInt32;
}

struct Devme{
  cameraName @0 : Text;
  image @1 : ImDat;
  sensor @2 : Sensor;
  totalFrames @3 : UInt32;
}

struct Sensor{
  sensorX @0 : UInt32;
  sensorY @1 : UInt32;
  timings @2 : Time; 
}

struct SDList {
  sundates @0 :List(Sundata);
}

struct NestedList {
  list @0 :List(List(Int32));
}

