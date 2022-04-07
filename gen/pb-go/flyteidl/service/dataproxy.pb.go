// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/service/dataproxy.proto

package service

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	duration "github.com/golang/protobuf/ptypes/duration"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	_ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
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

type CreateUploadLocationResponse struct {
	// SignedUrl specifies the url to use to upload content to (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...)
	SignedUrl string `protobuf:"bytes,1,opt,name=signed_url,json=signedUrl,proto3" json:"signed_url,omitempty"`
	// NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar)
	NativeUrl string `protobuf:"bytes,2,opt,name=native_url,json=nativeUrl,proto3" json:"native_url,omitempty"`
	// ExpiresAt defines when will the signed URL expires.
	ExpiresAt            *timestamp.Timestamp `protobuf:"bytes,3,opt,name=expires_at,json=expiresAt,proto3" json:"expires_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *CreateUploadLocationResponse) Reset()         { *m = CreateUploadLocationResponse{} }
func (m *CreateUploadLocationResponse) String() string { return proto.CompactTextString(m) }
func (*CreateUploadLocationResponse) ProtoMessage()    {}
func (*CreateUploadLocationResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_bffb71366d75dab0, []int{0}
}

func (m *CreateUploadLocationResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateUploadLocationResponse.Unmarshal(m, b)
}
func (m *CreateUploadLocationResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateUploadLocationResponse.Marshal(b, m, deterministic)
}
func (m *CreateUploadLocationResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateUploadLocationResponse.Merge(m, src)
}
func (m *CreateUploadLocationResponse) XXX_Size() int {
	return xxx_messageInfo_CreateUploadLocationResponse.Size(m)
}
func (m *CreateUploadLocationResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateUploadLocationResponse.DiscardUnknown(m)
}

var xxx_messageInfo_CreateUploadLocationResponse proto.InternalMessageInfo

func (m *CreateUploadLocationResponse) GetSignedUrl() string {
	if m != nil {
		return m.SignedUrl
	}
	return ""
}

func (m *CreateUploadLocationResponse) GetNativeUrl() string {
	if m != nil {
		return m.NativeUrl
	}
	return ""
}

func (m *CreateUploadLocationResponse) GetExpiresAt() *timestamp.Timestamp {
	if m != nil {
		return m.ExpiresAt
	}
	return nil
}

// CreateUploadLocationRequest specified request for the CreateUploadLocation API.
type CreateUploadLocationRequest struct {
	// Project to create the upload location for
	// +required
	Project string `protobuf:"bytes,1,opt,name=project,proto3" json:"project,omitempty"`
	// Domain to create the upload location for.
	// +required
	Domain string `protobuf:"bytes,2,opt,name=domain,proto3" json:"domain,omitempty"`
	// Suffix specifies a desired suffix for the generated location. E.g. `/file.py` or `pre/fix/file.zip`.
	// +optional. By default, the service will generate a consistent name based on the provided parameters.
	Suffix string `protobuf:"bytes,3,opt,name=suffix,proto3" json:"suffix,omitempty"`
	// ExpiresIn defines a requested expiration duration for the generated url. The request will be rejected if this
	// exceeds the platform allowed max.
	// +optional. The default value comes from a global config.
	ExpiresIn *duration.Duration `protobuf:"bytes,4,opt,name=expires_in,json=expiresIn,proto3" json:"expires_in,omitempty"`
	// ContentMD5 restricts the upload location to the specific MD5 provided. The ContentMD5 will also appear in the
	// generated path.
	// +required
	ContentMd5           []byte   `protobuf:"bytes,5,opt,name=content_md5,json=contentMd5,proto3" json:"content_md5,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CreateUploadLocationRequest) Reset()         { *m = CreateUploadLocationRequest{} }
func (m *CreateUploadLocationRequest) String() string { return proto.CompactTextString(m) }
func (*CreateUploadLocationRequest) ProtoMessage()    {}
func (*CreateUploadLocationRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_bffb71366d75dab0, []int{1}
}

func (m *CreateUploadLocationRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateUploadLocationRequest.Unmarshal(m, b)
}
func (m *CreateUploadLocationRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateUploadLocationRequest.Marshal(b, m, deterministic)
}
func (m *CreateUploadLocationRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateUploadLocationRequest.Merge(m, src)
}
func (m *CreateUploadLocationRequest) XXX_Size() int {
	return xxx_messageInfo_CreateUploadLocationRequest.Size(m)
}
func (m *CreateUploadLocationRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateUploadLocationRequest.DiscardUnknown(m)
}

var xxx_messageInfo_CreateUploadLocationRequest proto.InternalMessageInfo

func (m *CreateUploadLocationRequest) GetProject() string {
	if m != nil {
		return m.Project
	}
	return ""
}

func (m *CreateUploadLocationRequest) GetDomain() string {
	if m != nil {
		return m.Domain
	}
	return ""
}

func (m *CreateUploadLocationRequest) GetSuffix() string {
	if m != nil {
		return m.Suffix
	}
	return ""
}

func (m *CreateUploadLocationRequest) GetExpiresIn() *duration.Duration {
	if m != nil {
		return m.ExpiresIn
	}
	return nil
}

func (m *CreateUploadLocationRequest) GetContentMd5() []byte {
	if m != nil {
		return m.ContentMd5
	}
	return nil
}

func init() {
	proto.RegisterType((*CreateUploadLocationResponse)(nil), "flyteidl.service.CreateUploadLocationResponse")
	proto.RegisterType((*CreateUploadLocationRequest)(nil), "flyteidl.service.CreateUploadLocationRequest")
}

func init() { proto.RegisterFile("flyteidl/service/dataproxy.proto", fileDescriptor_bffb71366d75dab0) }

var fileDescriptor_bffb71366d75dab0 = []byte{
	// 496 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x93, 0x41, 0x6e, 0x13, 0x31,
	0x14, 0x86, 0x35, 0x01, 0x8a, 0xe2, 0xb2, 0xa8, 0x46, 0x08, 0x85, 0x50, 0x5a, 0x2b, 0x6c, 0x22,
	0x44, 0xc6, 0xa2, 0xa8, 0x82, 0xb2, 0x2b, 0x74, 0x83, 0xa0, 0x12, 0x0a, 0x74, 0xc3, 0x26, 0x7a,
	0x99, 0x79, 0xe3, 0x18, 0x26, 0xb6, 0xb1, 0xdf, 0xa4, 0xc9, 0x16, 0x89, 0x0b, 0xc0, 0x82, 0xfb,
	0x70, 0x05, 0xae, 0xc0, 0x01, 0x38, 0x02, 0x8a, 0xc7, 0x69, 0xa5, 0x10, 0xa1, 0xae, 0x46, 0xef,
	0xbd, 0xcf, 0xa3, 0xcf, 0xf6, 0x6f, 0xc6, 0xcb, 0x6a, 0x41, 0xa8, 0x8a, 0x4a, 0x78, 0x74, 0x33,
	0x95, 0xa3, 0x28, 0x80, 0xc0, 0x3a, 0x33, 0x5f, 0x64, 0xd6, 0x19, 0x32, 0xe9, 0xce, 0x8a, 0xc8,
	0x22, 0xd1, 0xdd, 0x95, 0xc6, 0xc8, 0x0a, 0x05, 0x58, 0x25, 0x40, 0x6b, 0x43, 0x40, 0xca, 0x68,
	0xdf, 0xf0, 0xdd, 0x47, 0xe1, 0x93, 0x0f, 0x24, 0xea, 0x81, 0x3f, 0x07, 0x29, 0xd1, 0x09, 0x63,
	0x03, 0xb1, 0x81, 0xde, 0x8b, 0xff, 0x0a, 0xd5, 0xb8, 0x2e, 0x45, 0x51, 0xbb, 0x00, 0xc4, 0xf9,
	0xfe, 0xfa, 0x9c, 0xd4, 0x14, 0x3d, 0xc1, 0xd4, 0x36, 0x40, 0xef, 0x47, 0xc2, 0x76, 0x5f, 0x3a,
	0x04, 0xc2, 0x33, 0x5b, 0x19, 0x28, 0xde, 0x98, 0x3c, 0xac, 0x1f, 0xa2, 0xb7, 0x46, 0x7b, 0x4c,
	0xef, 0x33, 0xe6, 0x95, 0xd4, 0x58, 0x8c, 0x6a, 0x57, 0x75, 0x12, 0x9e, 0xf4, 0xdb, 0xc3, 0x76,
	0xd3, 0x39, 0x73, 0xd5, 0x72, 0xac, 0x81, 0xd4, 0x0c, 0xc3, 0xb8, 0xd5, 0x8c, 0x9b, 0xce, 0x72,
	0x7c, 0xc4, 0x18, 0xce, 0xad, 0x72, 0xe8, 0x47, 0x40, 0x9d, 0x6b, 0x3c, 0xe9, 0x6f, 0x1f, 0x74,
	0xb3, 0x46, 0x2a, 0x5b, 0x49, 0x65, 0xef, 0x57, 0x52, 0xc3, 0x76, 0xa4, 0x8f, 0xa9, 0xf7, 0x33,
	0x61, 0xf7, 0x36, 0x9b, 0x7d, 0xae, 0xd1, 0x53, 0xda, 0x61, 0x37, 0xad, 0x33, 0x1f, 0x31, 0xa7,
	0x68, 0xb5, 0x2a, 0xd3, 0x3b, 0x6c, 0xab, 0x30, 0x53, 0x50, 0x3a, 0xfa, 0xc4, 0x6a, 0xd9, 0xf7,
	0x75, 0x59, 0xaa, 0x79, 0x10, 0x69, 0x0f, 0x63, 0x95, 0x3e, 0xbb, 0x94, 0x54, 0xba, 0x73, 0x3d,
	0x48, 0xde, 0xfd, 0x47, 0xf2, 0x24, 0x9e, 0xec, 0x85, 0xe3, 0x2b, 0x9d, 0xee, 0xb3, 0xed, 0xdc,
	0x68, 0x42, 0x4d, 0xa3, 0x69, 0x71, 0xd8, 0xb9, 0xc1, 0x93, 0xfe, 0xad, 0x21, 0x8b, 0xad, 0xd3,
	0xe2, 0xf0, 0xe0, 0x6b, 0x8b, 0xed, 0x9c, 0x00, 0xc1, 0xdb, 0x65, 0x22, 0xde, 0x35, 0x01, 0x48,
	0xff, 0x24, 0xec, 0xf6, 0xa6, 0x9d, 0xa5, 0x83, 0x6c, 0x3d, 0x2c, 0xd9, 0x7f, 0x4e, 0xa0, 0x9b,
	0x5d, 0x15, 0x6f, 0xae, 0xb2, 0xb7, 0xf8, 0x76, 0x7c, 0xda, 0x7d, 0xdd, 0x20, 0x9e, 0x03, 0x3f,
	0x77, 0x8a, 0x70, 0x60, 0x74, 0xb5, 0xe0, 0x13, 0x22, 0xcb, 0xab, 0xb8, 0x80, 0xd3, 0x04, 0x88,
	0x2b, 0xcf, 0x21, 0xcf, 0xd1, 0x7b, 0x35, 0xae, 0x90, 0x97, 0xc6, 0x71, 0x02, 0xff, 0xc9, 0x73,
	0x20, 0xee, 0x6a, 0xbd, 0xcc, 0x51, 0xf6, 0xe5, 0xd7, 0xef, 0xef, 0xad, 0x07, 0xbd, 0xbd, 0x10,
	0xe5, 0xd9, 0xe3, 0xcb, 0xec, 0x0b, 0x70, 0xa4, 0x4a, 0xc8, 0x69, 0x54, 0x3b, 0xfd, 0x3c, 0x79,
	0xf8, 0xe2, 0xe8, 0xc3, 0x53, 0xa9, 0x68, 0x52, 0x8f, 0xb3, 0xdc, 0x4c, 0x45, 0xd0, 0x36, 0x4e,
	0x8a, 0x8b, 0xd7, 0x23, 0x51, 0x0b, 0x3b, 0x1e, 0x48, 0x23, 0xd6, 0x1f, 0xd4, 0x78, 0x2b, 0xdc,
	0xc0, 0x93, 0xbf, 0x01, 0x00, 0x00, 0xff, 0xff, 0xcf, 0x56, 0xa2, 0xd7, 0x6b, 0x03, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// DataProxyServiceClient is the client API for DataProxyService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DataProxyServiceClient interface {
	// CreateUploadLocation creates a signed url to upload artifacts to for a given project/domain.
	CreateUploadLocation(ctx context.Context, in *CreateUploadLocationRequest, opts ...grpc.CallOption) (*CreateUploadLocationResponse, error)
}

type dataProxyServiceClient struct {
	cc *grpc.ClientConn
}

func NewDataProxyServiceClient(cc *grpc.ClientConn) DataProxyServiceClient {
	return &dataProxyServiceClient{cc}
}

func (c *dataProxyServiceClient) CreateUploadLocation(ctx context.Context, in *CreateUploadLocationRequest, opts ...grpc.CallOption) (*CreateUploadLocationResponse, error) {
	out := new(CreateUploadLocationResponse)
	err := c.cc.Invoke(ctx, "/flyteidl.service.DataProxyService/CreateUploadLocation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DataProxyServiceServer is the server API for DataProxyService service.
type DataProxyServiceServer interface {
	// CreateUploadLocation creates a signed url to upload artifacts to for a given project/domain.
	CreateUploadLocation(context.Context, *CreateUploadLocationRequest) (*CreateUploadLocationResponse, error)
}

// UnimplementedDataProxyServiceServer can be embedded to have forward compatible implementations.
type UnimplementedDataProxyServiceServer struct {
}

func (*UnimplementedDataProxyServiceServer) CreateUploadLocation(ctx context.Context, req *CreateUploadLocationRequest) (*CreateUploadLocationResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateUploadLocation not implemented")
}

func RegisterDataProxyServiceServer(s *grpc.Server, srv DataProxyServiceServer) {
	s.RegisterService(&_DataProxyService_serviceDesc, srv)
}

func _DataProxyService_CreateUploadLocation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateUploadLocationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataProxyServiceServer).CreateUploadLocation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/flyteidl.service.DataProxyService/CreateUploadLocation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataProxyServiceServer).CreateUploadLocation(ctx, req.(*CreateUploadLocationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _DataProxyService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "flyteidl.service.DataProxyService",
	HandlerType: (*DataProxyServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateUploadLocation",
			Handler:    _DataProxyService_CreateUploadLocation_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "flyteidl/service/dataproxy.proto",
}
