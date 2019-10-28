// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/plugins/qubole.proto

package plugins

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/lyft/flyteidl/gen/pb-go/flyteidl/core"
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

// Defines a query to execute on a hive cluster.
type HiveQuery struct {
	Query                string   `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	TimeoutSec           uint32   `protobuf:"varint,2,opt,name=timeout_sec,json=timeoutSec,proto3" json:"timeout_sec,omitempty"`
	RetryCount           uint32   `protobuf:"varint,3,opt,name=retryCount,proto3" json:"retryCount,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *HiveQuery) Reset()         { *m = HiveQuery{} }
func (m *HiveQuery) String() string { return proto.CompactTextString(m) }
func (*HiveQuery) ProtoMessage()    {}
func (*HiveQuery) Descriptor() ([]byte, []int) {
	return fileDescriptor_7cb86d766c12ee2e, []int{0}
}

func (m *HiveQuery) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_HiveQuery.Unmarshal(m, b)
}
func (m *HiveQuery) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_HiveQuery.Marshal(b, m, deterministic)
}
func (m *HiveQuery) XXX_Merge(src proto.Message) {
	xxx_messageInfo_HiveQuery.Merge(m, src)
}
func (m *HiveQuery) XXX_Size() int {
	return xxx_messageInfo_HiveQuery.Size(m)
}
func (m *HiveQuery) XXX_DiscardUnknown() {
	xxx_messageInfo_HiveQuery.DiscardUnknown(m)
}

var xxx_messageInfo_HiveQuery proto.InternalMessageInfo

func (m *HiveQuery) GetQuery() string {
	if m != nil {
		return m.Query
	}
	return ""
}

func (m *HiveQuery) GetTimeoutSec() uint32 {
	if m != nil {
		return m.TimeoutSec
	}
	return 0
}

func (m *HiveQuery) GetRetryCount() uint32 {
	if m != nil {
		return m.RetryCount
	}
	return 0
}

// Defines a collection of hive queries.
type HiveQueryCollection struct {
	Queries              []*HiveQuery `protobuf:"bytes,2,rep,name=queries,proto3" json:"queries,omitempty"`
	XXX_NoUnkeyedLiteral struct{}     `json:"-"`
	XXX_unrecognized     []byte       `json:"-"`
	XXX_sizecache        int32        `json:"-"`
}

func (m *HiveQueryCollection) Reset()         { *m = HiveQueryCollection{} }
func (m *HiveQueryCollection) String() string { return proto.CompactTextString(m) }
func (*HiveQueryCollection) ProtoMessage()    {}
func (*HiveQueryCollection) Descriptor() ([]byte, []int) {
	return fileDescriptor_7cb86d766c12ee2e, []int{1}
}

func (m *HiveQueryCollection) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_HiveQueryCollection.Unmarshal(m, b)
}
func (m *HiveQueryCollection) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_HiveQueryCollection.Marshal(b, m, deterministic)
}
func (m *HiveQueryCollection) XXX_Merge(src proto.Message) {
	xxx_messageInfo_HiveQueryCollection.Merge(m, src)
}
func (m *HiveQueryCollection) XXX_Size() int {
	return xxx_messageInfo_HiveQueryCollection.Size(m)
}
func (m *HiveQueryCollection) XXX_DiscardUnknown() {
	xxx_messageInfo_HiveQueryCollection.DiscardUnknown(m)
}

var xxx_messageInfo_HiveQueryCollection proto.InternalMessageInfo

func (m *HiveQueryCollection) GetQueries() []*HiveQuery {
	if m != nil {
		return m.Queries
	}
	return nil
}

// This message works with the 'hive' task type in the SDK and is the object that will be in the 'custom' field
// of a hive task's TaskTemplate
type QuboleHiveJob struct {
	ClusterLabel         string               `protobuf:"bytes,1,opt,name=cluster_label,json=clusterLabel,proto3" json:"cluster_label,omitempty"`
	QueryCollection      *HiveQueryCollection `protobuf:"bytes,2,opt,name=query_collection,json=queryCollection,proto3" json:"query_collection,omitempty"` // Deprecated: Do not use.
	Tags                 []string             `protobuf:"bytes,3,rep,name=tags,proto3" json:"tags,omitempty"`
	Query                *HiveQuery           `protobuf:"bytes,4,opt,name=query,proto3" json:"query,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *QuboleHiveJob) Reset()         { *m = QuboleHiveJob{} }
func (m *QuboleHiveJob) String() string { return proto.CompactTextString(m) }
func (*QuboleHiveJob) ProtoMessage()    {}
func (*QuboleHiveJob) Descriptor() ([]byte, []int) {
	return fileDescriptor_7cb86d766c12ee2e, []int{2}
}

func (m *QuboleHiveJob) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_QuboleHiveJob.Unmarshal(m, b)
}
func (m *QuboleHiveJob) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_QuboleHiveJob.Marshal(b, m, deterministic)
}
func (m *QuboleHiveJob) XXX_Merge(src proto.Message) {
	xxx_messageInfo_QuboleHiveJob.Merge(m, src)
}
func (m *QuboleHiveJob) XXX_Size() int {
	return xxx_messageInfo_QuboleHiveJob.Size(m)
}
func (m *QuboleHiveJob) XXX_DiscardUnknown() {
	xxx_messageInfo_QuboleHiveJob.DiscardUnknown(m)
}

var xxx_messageInfo_QuboleHiveJob proto.InternalMessageInfo

func (m *QuboleHiveJob) GetClusterLabel() string {
	if m != nil {
		return m.ClusterLabel
	}
	return ""
}

// Deprecated: Do not use.
func (m *QuboleHiveJob) GetQueryCollection() *HiveQueryCollection {
	if m != nil {
		return m.QueryCollection
	}
	return nil
}

func (m *QuboleHiveJob) GetTags() []string {
	if m != nil {
		return m.Tags
	}
	return nil
}

func (m *QuboleHiveJob) GetQuery() *HiveQuery {
	if m != nil {
		return m.Query
	}
	return nil
}

func init() {
	proto.RegisterType((*HiveQuery)(nil), "flyteidl.plugins.HiveQuery")
	proto.RegisterType((*HiveQueryCollection)(nil), "flyteidl.plugins.HiveQueryCollection")
	proto.RegisterType((*QuboleHiveJob)(nil), "flyteidl.plugins.QuboleHiveJob")
}

func init() { proto.RegisterFile("flyteidl/plugins/qubole.proto", fileDescriptor_7cb86d766c12ee2e) }

var fileDescriptor_7cb86d766c12ee2e = []byte{
	// 316 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x7c, 0x51, 0xc1, 0x4e, 0xc2, 0x40,
	0x14, 0x4c, 0x29, 0x6a, 0x78, 0x48, 0x24, 0xab, 0x87, 0xaa, 0x51, 0x1b, 0x8c, 0x49, 0x2f, 0x76,
	0x23, 0x84, 0x1f, 0x80, 0x8b, 0x31, 0x5c, 0xa8, 0x9e, 0xbc, 0x10, 0x76, 0x7d, 0xd4, 0x8d, 0x4b,
	0x17, 0xba, 0xbb, 0x26, 0xfd, 0x4c, 0xff, 0xc8, 0x74, 0x5b, 0x4a, 0xc2, 0x81, 0xdb, 0xeb, 0xcc,
	0x7b, 0x9d, 0x99, 0x1d, 0xb8, 0x5b, 0xc9, 0xc2, 0xa0, 0xf8, 0x92, 0x74, 0x23, 0x6d, 0x2a, 0x32,
	0x4d, 0xb7, 0x96, 0x29, 0x89, 0xf1, 0x26, 0x57, 0x46, 0x91, 0xfe, 0x8e, 0x8e, 0x6b, 0xfa, 0xe6,
	0xba, 0x39, 0xe0, 0x2a, 0x47, 0x6a, 0x96, 0xfa, 0x47, 0x57, 0xcb, 0x03, 0x06, 0x9d, 0x57, 0xf1,
	0x8b, 0x73, 0x8b, 0x79, 0x41, 0xae, 0xe0, 0x64, 0x5b, 0x0e, 0x81, 0x17, 0x7a, 0x51, 0x27, 0xa9,
	0x3e, 0xc8, 0x03, 0x74, 0x8d, 0x58, 0xa3, 0xb2, 0x66, 0xa1, 0x91, 0x07, 0xad, 0xd0, 0x8b, 0x7a,
	0x09, 0xd4, 0xd0, 0x3b, 0x72, 0x72, 0x0f, 0x90, 0xa3, 0xc9, 0x8b, 0xa9, 0xb2, 0x99, 0x09, 0xfc,
	0x8a, 0xdf, 0x23, 0x83, 0x19, 0x5c, 0x36, 0x1a, 0x53, 0x25, 0x25, 0x72, 0x23, 0x54, 0x46, 0xc6,
	0x70, 0x56, 0x0a, 0x08, 0xd4, 0x41, 0x2b, 0xf4, 0xa3, 0xee, 0xf0, 0x36, 0x3e, 0x74, 0x1e, 0x37,
	0x77, 0xc9, 0x6e, 0x77, 0xf0, 0xe7, 0x41, 0x6f, 0xee, 0xf2, 0x96, 0xe4, 0x9b, 0x62, 0xe4, 0x11,
	0x7a, 0x5c, 0x5a, 0x6d, 0x30, 0x5f, 0xc8, 0x25, 0x43, 0x59, 0xdb, 0x3f, 0xaf, 0xc1, 0x59, 0x89,
	0x91, 0x0f, 0xe8, 0xbb, 0x38, 0x0b, 0xde, 0x38, 0x70, 0x51, 0xba, 0xc3, 0xa7, 0x23, 0xb2, 0x7b,
	0xbb, 0x93, 0x56, 0xe0, 0x25, 0x17, 0xdb, 0x83, 0x0c, 0x04, 0xda, 0x66, 0x99, 0xea, 0xc0, 0x0f,
	0xfd, 0xa8, 0x93, 0xb8, 0x99, 0xbc, 0xec, 0x5e, 0xb1, 0xed, 0x7e, 0x7f, 0x34, 0x55, 0xb5, 0x39,
	0x19, 0x7f, 0x8e, 0x52, 0x61, 0xbe, 0x2d, 0x8b, 0xb9, 0x5a, 0x53, 0x59, 0xac, 0x0c, 0x6d, 0x2a,
	0x4b, 0x31, 0xa3, 0x1b, 0xf6, 0x9c, 0x2a, 0x7a, 0x58, 0x3b, 0x3b, 0x75, 0x1d, 0x8e, 0xfe, 0x03,
	0x00, 0x00, 0xff, 0xff, 0x63, 0xd9, 0xa0, 0x6e, 0x11, 0x02, 0x00, 0x00,
}
