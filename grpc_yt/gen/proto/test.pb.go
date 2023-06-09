// Code generated by protoc-gen-go. DO NOT EDIT.
// source: test.proto

package proto

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Coordinates struct {
	Cx                   float32  `protobuf:"fixed32,1,opt,name=cx,proto3" json:"cx,omitempty"`
	Cy                   float32  `protobuf:"fixed32,2,opt,name=cy,proto3" json:"cy,omitempty"`
	Time                 float32  `protobuf:"fixed32,3,opt,name=time,proto3" json:"time,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Coordinates) Reset()         { *m = Coordinates{} }
func (m *Coordinates) String() string { return proto.CompactTextString(m) }
func (*Coordinates) ProtoMessage()    {}
func (*Coordinates) Descriptor() ([]byte, []int) {
	return fileDescriptor_c161fcfdc0c3ff1e, []int{0}
}

func (m *Coordinates) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Coordinates.Unmarshal(m, b)
}
func (m *Coordinates) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Coordinates.Marshal(b, m, deterministic)
}
func (m *Coordinates) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Coordinates.Merge(m, src)
}
func (m *Coordinates) XXX_Size() int {
	return xxx_messageInfo_Coordinates.Size(m)
}
func (m *Coordinates) XXX_DiscardUnknown() {
	xxx_messageInfo_Coordinates.DiscardUnknown(m)
}

var xxx_messageInfo_Coordinates proto.InternalMessageInfo

func (m *Coordinates) GetCx() float32 {
	if m != nil {
		return m.Cx
	}
	return 0
}

func (m *Coordinates) GetCy() float32 {
	if m != nil {
		return m.Cy
	}
	return 0
}

func (m *Coordinates) GetTime() float32 {
	if m != nil {
		return m.Time
	}
	return 0
}

type Empty struct {
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Empty) Reset()         { *m = Empty{} }
func (m *Empty) String() string { return proto.CompactTextString(m) }
func (*Empty) ProtoMessage()    {}
func (*Empty) Descriptor() ([]byte, []int) {
	return fileDescriptor_c161fcfdc0c3ff1e, []int{1}
}

func (m *Empty) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Empty.Unmarshal(m, b)
}
func (m *Empty) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Empty.Marshal(b, m, deterministic)
}
func (m *Empty) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Empty.Merge(m, src)
}
func (m *Empty) XXX_Size() int {
	return xxx_messageInfo_Empty.Size(m)
}
func (m *Empty) XXX_DiscardUnknown() {
	xxx_messageInfo_Empty.DiscardUnknown(m)
}

var xxx_messageInfo_Empty proto.InternalMessageInfo

func init() {
	proto.RegisterType((*Coordinates)(nil), "multiplied_coordinates.Coordinates")
	proto.RegisterType((*Empty)(nil), "multiplied_coordinates.Empty")
}

func init() { proto.RegisterFile("test.proto", fileDescriptor_c161fcfdc0c3ff1e) }

var fileDescriptor_c161fcfdc0c3ff1e = []byte{
	// 203 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x2a, 0x49, 0x2d, 0x2e,
	0xd1, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x12, 0xcb, 0x2d, 0xcd, 0x29, 0xc9, 0x2c, 0xc8, 0xc9,
	0x4c, 0x4d, 0x89, 0x4f, 0xce, 0xcf, 0x2f, 0x4a, 0xc9, 0xcc, 0x4b, 0x2c, 0x49, 0x2d, 0x96, 0x92,
	0x49, 0xcf, 0xcf, 0x4f, 0xcf, 0x49, 0xd5, 0x4f, 0x2c, 0xc8, 0xd4, 0x4f, 0xcc, 0xcb, 0xcb, 0x2f,
	0x49, 0x2c, 0xc9, 0xcc, 0xcf, 0x2b, 0x86, 0xe8, 0x52, 0x72, 0xe4, 0xe2, 0x76, 0x46, 0x28, 0x16,
	0xe2, 0xe3, 0x62, 0x4a, 0xae, 0x90, 0x60, 0x54, 0x60, 0xd4, 0x60, 0x0a, 0x62, 0x4a, 0xae, 0x00,
	0xf3, 0x2b, 0x25, 0x98, 0xa0, 0xfc, 0x4a, 0x21, 0x21, 0x2e, 0x96, 0x92, 0xcc, 0xdc, 0x54, 0x09,
	0x66, 0xb0, 0x08, 0x98, 0xad, 0xc4, 0xce, 0xc5, 0xea, 0x9a, 0x5b, 0x50, 0x52, 0x69, 0x54, 0xc5,
	0x25, 0x88, 0x30, 0x2b, 0x38, 0xb5, 0xa8, 0x2c, 0x33, 0x39, 0x55, 0x28, 0x95, 0x8b, 0xcf, 0x3d,
	0xb5, 0x04, 0xd9, 0x0e, 0x59, 0x3d, 0xec, 0x2e, 0xd5, 0x03, 0x9b, 0x22, 0xa5, 0x8c, 0x4b, 0x1a,
	0xc9, 0x0c, 0x25, 0xfe, 0xa6, 0xcb, 0x4f, 0x26, 0x33, 0x71, 0x0a, 0xb1, 0xeb, 0x83, 0x55, 0x14,
	0x3b, 0x71, 0x46, 0xb1, 0xeb, 0xe9, 0x83, 0xbd, 0x94, 0xc4, 0x06, 0xa6, 0x8c, 0x01, 0x01, 0x00,
	0x00, 0xff, 0xff, 0x2d, 0xb6, 0xe0, 0x6f, 0x1d, 0x01, 0x00, 0x00,
}
