// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/admin/schedule.proto

package admin

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
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

// Represents a frequency at which to run a schedule.
type FixedRateUnit int32

const (
	FixedRateUnit_MINUTE FixedRateUnit = 0
	FixedRateUnit_HOUR   FixedRateUnit = 1
	FixedRateUnit_DAY    FixedRateUnit = 2
)

var FixedRateUnit_name = map[int32]string{
	0: "MINUTE",
	1: "HOUR",
	2: "DAY",
}

var FixedRateUnit_value = map[string]int32{
	"MINUTE": 0,
	"HOUR":   1,
	"DAY":    2,
}

func (x FixedRateUnit) String() string {
	return proto.EnumName(FixedRateUnit_name, int32(x))
}

func (FixedRateUnit) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_a71cf75647fcd25a, []int{0}
}

// Option for schedules run at a certain frequency, e.g. every 2 minutes.
type FixedRate struct {
	Value                uint32        `protobuf:"varint,1,opt,name=value,proto3" json:"value,omitempty"`
	Unit                 FixedRateUnit `protobuf:"varint,2,opt,name=unit,proto3,enum=flyteidl.admin.FixedRateUnit" json:"unit,omitempty"`
	XXX_NoUnkeyedLiteral struct{}      `json:"-"`
	XXX_unrecognized     []byte        `json:"-"`
	XXX_sizecache        int32         `json:"-"`
}

func (m *FixedRate) Reset()         { *m = FixedRate{} }
func (m *FixedRate) String() string { return proto.CompactTextString(m) }
func (*FixedRate) ProtoMessage()    {}
func (*FixedRate) Descriptor() ([]byte, []int) {
	return fileDescriptor_a71cf75647fcd25a, []int{0}
}

func (m *FixedRate) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FixedRate.Unmarshal(m, b)
}
func (m *FixedRate) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FixedRate.Marshal(b, m, deterministic)
}
func (m *FixedRate) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FixedRate.Merge(m, src)
}
func (m *FixedRate) XXX_Size() int {
	return xxx_messageInfo_FixedRate.Size(m)
}
func (m *FixedRate) XXX_DiscardUnknown() {
	xxx_messageInfo_FixedRate.DiscardUnknown(m)
}

var xxx_messageInfo_FixedRate proto.InternalMessageInfo

func (m *FixedRate) GetValue() uint32 {
	if m != nil {
		return m.Value
	}
	return 0
}

func (m *FixedRate) GetUnit() FixedRateUnit {
	if m != nil {
		return m.Unit
	}
	return FixedRateUnit_MINUTE
}

type CronSchedule struct {
	// Standard/default cron implementation as described by https://en.wikipedia.org/wiki/Cron#CRON_expression;
	// Also supports nonstandard predefined scheduling definitions
	// as described by https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
	// except @reboot
	Schedule string `protobuf:"bytes,1,opt,name=schedule,proto3" json:"schedule,omitempty"`
	// ISO 8601 duration as described by https://en.wikipedia.org/wiki/ISO_8601#Durations
	Offset               string   `protobuf:"bytes,2,opt,name=offset,proto3" json:"offset,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CronSchedule) Reset()         { *m = CronSchedule{} }
func (m *CronSchedule) String() string { return proto.CompactTextString(m) }
func (*CronSchedule) ProtoMessage()    {}
func (*CronSchedule) Descriptor() ([]byte, []int) {
	return fileDescriptor_a71cf75647fcd25a, []int{1}
}

func (m *CronSchedule) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CronSchedule.Unmarshal(m, b)
}
func (m *CronSchedule) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CronSchedule.Marshal(b, m, deterministic)
}
func (m *CronSchedule) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CronSchedule.Merge(m, src)
}
func (m *CronSchedule) XXX_Size() int {
	return xxx_messageInfo_CronSchedule.Size(m)
}
func (m *CronSchedule) XXX_DiscardUnknown() {
	xxx_messageInfo_CronSchedule.DiscardUnknown(m)
}

var xxx_messageInfo_CronSchedule proto.InternalMessageInfo

func (m *CronSchedule) GetSchedule() string {
	if m != nil {
		return m.Schedule
	}
	return ""
}

func (m *CronSchedule) GetOffset() string {
	if m != nil {
		return m.Offset
	}
	return ""
}

// Defines complete set of information required to trigger an execution on a schedule.
type Schedule struct {
	// Types that are valid to be assigned to ScheduleExpression:
	//	*Schedule_CronExpression
	//	*Schedule_Rate
	//	*Schedule_CronSchedule
	ScheduleExpression isSchedule_ScheduleExpression `protobuf_oneof:"ScheduleExpression"`
	// Name of the input variable that the kickoff time will be supplied to when the workflow is kicked off.
	KickoffTimeInputArg  string   `protobuf:"bytes,3,opt,name=kickoff_time_input_arg,json=kickoffTimeInputArg,proto3" json:"kickoff_time_input_arg,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Schedule) Reset()         { *m = Schedule{} }
func (m *Schedule) String() string { return proto.CompactTextString(m) }
func (*Schedule) ProtoMessage()    {}
func (*Schedule) Descriptor() ([]byte, []int) {
	return fileDescriptor_a71cf75647fcd25a, []int{2}
}

func (m *Schedule) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Schedule.Unmarshal(m, b)
}
func (m *Schedule) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Schedule.Marshal(b, m, deterministic)
}
func (m *Schedule) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Schedule.Merge(m, src)
}
func (m *Schedule) XXX_Size() int {
	return xxx_messageInfo_Schedule.Size(m)
}
func (m *Schedule) XXX_DiscardUnknown() {
	xxx_messageInfo_Schedule.DiscardUnknown(m)
}

var xxx_messageInfo_Schedule proto.InternalMessageInfo

type isSchedule_ScheduleExpression interface {
	isSchedule_ScheduleExpression()
}

type Schedule_CronExpression struct {
	CronExpression string `protobuf:"bytes,1,opt,name=cron_expression,json=cronExpression,proto3,oneof"`
}

type Schedule_Rate struct {
	Rate *FixedRate `protobuf:"bytes,2,opt,name=rate,proto3,oneof"`
}

type Schedule_CronSchedule struct {
	CronSchedule *CronSchedule `protobuf:"bytes,4,opt,name=cron_schedule,json=cronSchedule,proto3,oneof"`
}

func (*Schedule_CronExpression) isSchedule_ScheduleExpression() {}

func (*Schedule_Rate) isSchedule_ScheduleExpression() {}

func (*Schedule_CronSchedule) isSchedule_ScheduleExpression() {}

func (m *Schedule) GetScheduleExpression() isSchedule_ScheduleExpression {
	if m != nil {
		return m.ScheduleExpression
	}
	return nil
}

// Deprecated: Do not use.
func (m *Schedule) GetCronExpression() string {
	if x, ok := m.GetScheduleExpression().(*Schedule_CronExpression); ok {
		return x.CronExpression
	}
	return ""
}

func (m *Schedule) GetRate() *FixedRate {
	if x, ok := m.GetScheduleExpression().(*Schedule_Rate); ok {
		return x.Rate
	}
	return nil
}

func (m *Schedule) GetCronSchedule() *CronSchedule {
	if x, ok := m.GetScheduleExpression().(*Schedule_CronSchedule); ok {
		return x.CronSchedule
	}
	return nil
}

func (m *Schedule) GetKickoffTimeInputArg() string {
	if m != nil {
		return m.KickoffTimeInputArg
	}
	return ""
}

// XXX_OneofWrappers is for the internal use of the proto package.
func (*Schedule) XXX_OneofWrappers() []interface{} {
	return []interface{}{
		(*Schedule_CronExpression)(nil),
		(*Schedule_Rate)(nil),
		(*Schedule_CronSchedule)(nil),
	}
}

func init() {
	proto.RegisterEnum("flyteidl.admin.FixedRateUnit", FixedRateUnit_name, FixedRateUnit_value)
	proto.RegisterType((*FixedRate)(nil), "flyteidl.admin.FixedRate")
	proto.RegisterType((*CronSchedule)(nil), "flyteidl.admin.CronSchedule")
	proto.RegisterType((*Schedule)(nil), "flyteidl.admin.Schedule")
}

func init() { proto.RegisterFile("flyteidl/admin/schedule.proto", fileDescriptor_a71cf75647fcd25a) }

var fileDescriptor_a71cf75647fcd25a = []byte{
	// 358 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x74, 0x92, 0xc1, 0x8b, 0xda, 0x40,
	0x14, 0xc6, 0x13, 0x4d, 0xad, 0xbe, 0xaa, 0x95, 0xa9, 0x48, 0x5a, 0x2a, 0x88, 0x27, 0x29, 0x98,
	0x50, 0xa5, 0xf4, 0x6c, 0xac, 0x25, 0x1e, 0x76, 0x17, 0x66, 0xf5, 0xb0, 0x7b, 0x09, 0x31, 0x99,
	0xc4, 0xc1, 0x64, 0x26, 0x4c, 0x26, 0x8b, 0xfb, 0xaf, 0xef, 0x69, 0x71, 0xd4, 0xac, 0x2e, 0xec,
	0xf1, 0xf1, 0xcd, 0xfb, 0xbd, 0xef, 0x1b, 0x3e, 0xe8, 0x47, 0xc9, 0xb3, 0x24, 0x34, 0x4c, 0x6c,
	0x3f, 0x4c, 0x29, 0xb3, 0xf3, 0x60, 0x4b, 0xc2, 0x22, 0x21, 0x56, 0x26, 0xb8, 0xe4, 0xa8, 0x7d,
	0x96, 0x2d, 0x25, 0x0f, 0x57, 0xd0, 0xf8, 0x4f, 0xf7, 0x24, 0xc4, 0xbe, 0x24, 0xa8, 0x0b, 0x9f,
	0x9e, 0xfc, 0xa4, 0x20, 0xa6, 0x3e, 0xd0, 0x47, 0x2d, 0x7c, 0x1c, 0xd0, 0x6f, 0x30, 0x0a, 0x46,
	0xa5, 0x59, 0x19, 0xe8, 0xa3, 0xf6, 0xa4, 0x6f, 0x5d, 0x13, 0xac, 0x72, 0x7d, 0xcd, 0xa8, 0xc4,
	0xea, 0xe9, 0xd0, 0x81, 0xe6, 0x5c, 0x70, 0x76, 0x7f, 0xba, 0x8d, 0x7e, 0x40, 0xfd, 0xec, 0x43,
	0xb1, 0x1b, 0xb8, 0x9c, 0x51, 0x0f, 0x6a, 0x3c, 0x8a, 0x72, 0x72, 0x3c, 0xd0, 0xc0, 0xa7, 0x69,
	0xf8, 0xa2, 0x43, 0xbd, 0x04, 0x8c, 0xe1, 0x6b, 0x20, 0x38, 0xf3, 0xc8, 0x3e, 0x13, 0x24, 0xcf,
	0x29, 0x67, 0x47, 0x8e, 0x53, 0x31, 0x75, 0x57, 0xc3, 0xed, 0x83, 0xb8, 0x28, 0x35, 0x64, 0x83,
	0x21, 0x7c, 0x49, 0x14, 0xf1, 0xcb, 0xe4, 0xfb, 0x87, 0x96, 0x5d, 0x0d, 0xab, 0x87, 0x68, 0x0e,
	0x2d, 0xc5, 0x2f, 0x5d, 0x1a, 0x6a, 0xf3, 0xe7, 0xfb, 0xcd, 0xcb, 0x54, 0xae, 0x86, 0x9b, 0xc1,
	0x65, 0xca, 0x29, 0xf4, 0x76, 0x34, 0xd8, 0xf1, 0x28, 0xf2, 0x24, 0x4d, 0x89, 0x47, 0x59, 0x56,
	0x48, 0xcf, 0x17, 0xb1, 0x59, 0x55, 0xc9, 0xbe, 0x9d, 0xd4, 0x15, 0x4d, 0xc9, 0xf2, 0xa0, 0xcd,
	0x44, 0xec, 0x74, 0x01, 0x9d, 0x01, 0x6f, 0x01, 0x7e, 0x59, 0xd0, 0xba, 0xfa, 0x57, 0x04, 0x50,
	0xbb, 0x59, 0xde, 0xae, 0x57, 0x8b, 0x8e, 0x86, 0xea, 0x60, 0xb8, 0x77, 0x6b, 0xdc, 0xd1, 0xd1,
	0x67, 0xa8, 0xfe, 0x9b, 0x3d, 0x74, 0x2a, 0xce, 0xdf, 0xc7, 0x3f, 0x31, 0x95, 0xdb, 0x62, 0x63,
	0x05, 0x3c, 0xb5, 0x95, 0x69, 0x2e, 0x62, 0xbb, 0xec, 0x42, 0x4c, 0x98, 0x9d, 0x6d, 0xc6, 0x31,
	0xb7, 0xaf, 0xeb, 0xb1, 0xa9, 0xa9, 0x5a, 0x4c, 0x5f, 0x03, 0x00, 0x00, 0xff, 0xff, 0x14, 0xbd,
	0x83, 0xd9, 0x37, 0x02, 0x00, 0x00,
}
