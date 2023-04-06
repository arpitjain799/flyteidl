// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/admin/data.proto

#ifndef PROTOBUF_INCLUDED_flyteidl_2fadmin_2fdata_2eproto
#define PROTOBUF_INCLUDED_flyteidl_2fadmin_2fdata_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3007000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3007000 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
#include "flyteidl/admin/common.pb.h"
#include "flyteidl/core/literals.pb.h"
#include "flyteidl/admin/node_execution.pb.h"
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_flyteidl_2fadmin_2fdata_2eproto

// Internal implementation detail -- do not use these members.
struct TableStruct_flyteidl_2fadmin_2fdata_2eproto {
  static const ::google::protobuf::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors_flyteidl_2fadmin_2fdata_2eproto();
namespace flyteidl {
namespace admin {
class DataResponse;
class DataResponseDefaultTypeInternal;
extern DataResponseDefaultTypeInternal _DataResponse_default_instance_;
class FlyteArtifactGetRequest;
class FlyteArtifactGetRequestDefaultTypeInternal;
extern FlyteArtifactGetRequestDefaultTypeInternal _FlyteArtifactGetRequest_default_instance_;
}  // namespace admin
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> ::flyteidl::admin::DataResponse* Arena::CreateMaybeMessage<::flyteidl::admin::DataResponse>(Arena*);
template<> ::flyteidl::admin::FlyteArtifactGetRequest* Arena::CreateMaybeMessage<::flyteidl::admin::FlyteArtifactGetRequest>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace flyteidl {
namespace admin {

// ===================================================================

class FlyteArtifactGetRequest final :
    public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:flyteidl.admin.FlyteArtifactGetRequest) */ {
 public:
  FlyteArtifactGetRequest();
  virtual ~FlyteArtifactGetRequest();

  FlyteArtifactGetRequest(const FlyteArtifactGetRequest& from);

  inline FlyteArtifactGetRequest& operator=(const FlyteArtifactGetRequest& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  FlyteArtifactGetRequest(FlyteArtifactGetRequest&& from) noexcept
    : FlyteArtifactGetRequest() {
    *this = ::std::move(from);
  }

  inline FlyteArtifactGetRequest& operator=(FlyteArtifactGetRequest&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor() {
    return default_instance().GetDescriptor();
  }
  static const FlyteArtifactGetRequest& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const FlyteArtifactGetRequest* internal_default_instance() {
    return reinterpret_cast<const FlyteArtifactGetRequest*>(
               &_FlyteArtifactGetRequest_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(FlyteArtifactGetRequest* other);
  friend void swap(FlyteArtifactGetRequest& a, FlyteArtifactGetRequest& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline FlyteArtifactGetRequest* New() const final {
    return CreateMaybeMessage<FlyteArtifactGetRequest>(nullptr);
  }

  FlyteArtifactGetRequest* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<FlyteArtifactGetRequest>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const FlyteArtifactGetRequest& from);
  void MergeFrom(const FlyteArtifactGetRequest& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  static const char* _InternalParse(const char* begin, const char* end, void* object, ::google::protobuf::internal::ParseContext* ctx);
  ::google::protobuf::internal::ParseFunc _ParseFunc() const final { return _InternalParse; }
  #else
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(FlyteArtifactGetRequest* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // .flyteidl.admin.FlyteArtifact artifact = 1;
  bool has_artifact() const;
  void clear_artifact();
  static const int kArtifactFieldNumber = 1;
  const ::flyteidl::admin::FlyteArtifact& artifact() const;
  ::flyteidl::admin::FlyteArtifact* release_artifact();
  ::flyteidl::admin::FlyteArtifact* mutable_artifact();
  void set_allocated_artifact(::flyteidl::admin::FlyteArtifact* artifact);

  // @@protoc_insertion_point(class_scope:flyteidl.admin.FlyteArtifactGetRequest)
 private:
  class HasBitSetters;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::flyteidl::admin::FlyteArtifact* artifact_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_flyteidl_2fadmin_2fdata_2eproto;
};
// -------------------------------------------------------------------

class DataResponse final :
    public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:flyteidl.admin.DataResponse) */ {
 public:
  DataResponse();
  virtual ~DataResponse();

  DataResponse(const DataResponse& from);

  inline DataResponse& operator=(const DataResponse& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  DataResponse(DataResponse&& from) noexcept
    : DataResponse() {
    *this = ::std::move(from);
  }

  inline DataResponse& operator=(DataResponse&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor() {
    return default_instance().GetDescriptor();
  }
  static const DataResponse& default_instance();

  enum DataCase {
    kLiteralMap = 1,
    kFlyteDeck = 2,
    kDynamicWorkflow = 3,
    DATA_NOT_SET = 0,
  };

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const DataResponse* internal_default_instance() {
    return reinterpret_cast<const DataResponse*>(
               &_DataResponse_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  void Swap(DataResponse* other);
  friend void swap(DataResponse& a, DataResponse& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline DataResponse* New() const final {
    return CreateMaybeMessage<DataResponse>(nullptr);
  }

  DataResponse* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<DataResponse>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const DataResponse& from);
  void MergeFrom(const DataResponse& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  static const char* _InternalParse(const char* begin, const char* end, void* object, ::google::protobuf::internal::ParseContext* ctx);
  ::google::protobuf::internal::ParseFunc _ParseFunc() const final { return _InternalParse; }
  #else
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(DataResponse* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // .flyteidl.core.LiteralMap literal_map = 1;
  bool has_literal_map() const;
  void clear_literal_map();
  static const int kLiteralMapFieldNumber = 1;
  const ::flyteidl::core::LiteralMap& literal_map() const;
  ::flyteidl::core::LiteralMap* release_literal_map();
  ::flyteidl::core::LiteralMap* mutable_literal_map();
  void set_allocated_literal_map(::flyteidl::core::LiteralMap* literal_map);

  // bytes flyte_deck = 2;
  private:
  bool has_flyte_deck() const;
  public:
  void clear_flyte_deck();
  static const int kFlyteDeckFieldNumber = 2;
  const ::std::string& flyte_deck() const;
  void set_flyte_deck(const ::std::string& value);
  #if LANG_CXX11
  void set_flyte_deck(::std::string&& value);
  #endif
  void set_flyte_deck(const char* value);
  void set_flyte_deck(const void* value, size_t size);
  ::std::string* mutable_flyte_deck();
  ::std::string* release_flyte_deck();
  void set_allocated_flyte_deck(::std::string* flyte_deck);

  // .flyteidl.admin.DynamicWorkflowNodeMetadata dynamic_workflow = 3;
  bool has_dynamic_workflow() const;
  void clear_dynamic_workflow();
  static const int kDynamicWorkflowFieldNumber = 3;
  const ::flyteidl::admin::DynamicWorkflowNodeMetadata& dynamic_workflow() const;
  ::flyteidl::admin::DynamicWorkflowNodeMetadata* release_dynamic_workflow();
  ::flyteidl::admin::DynamicWorkflowNodeMetadata* mutable_dynamic_workflow();
  void set_allocated_dynamic_workflow(::flyteidl::admin::DynamicWorkflowNodeMetadata* dynamic_workflow);

  void clear_data();
  DataCase data_case() const;
  // @@protoc_insertion_point(class_scope:flyteidl.admin.DataResponse)
 private:
  class HasBitSetters;
  void set_has_literal_map();
  void set_has_flyte_deck();
  void set_has_dynamic_workflow();

  inline bool has_data() const;
  inline void clear_has_data();

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  union DataUnion {
    DataUnion() {}
    ::flyteidl::core::LiteralMap* literal_map_;
    ::google::protobuf::internal::ArenaStringPtr flyte_deck_;
    ::flyteidl::admin::DynamicWorkflowNodeMetadata* dynamic_workflow_;
  } data_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  ::google::protobuf::uint32 _oneof_case_[1];

  friend struct ::TableStruct_flyteidl_2fadmin_2fdata_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// FlyteArtifactGetRequest

// .flyteidl.admin.FlyteArtifact artifact = 1;
inline bool FlyteArtifactGetRequest::has_artifact() const {
  return this != internal_default_instance() && artifact_ != nullptr;
}
inline const ::flyteidl::admin::FlyteArtifact& FlyteArtifactGetRequest::artifact() const {
  const ::flyteidl::admin::FlyteArtifact* p = artifact_;
  // @@protoc_insertion_point(field_get:flyteidl.admin.FlyteArtifactGetRequest.artifact)
  return p != nullptr ? *p : *reinterpret_cast<const ::flyteidl::admin::FlyteArtifact*>(
      &::flyteidl::admin::_FlyteArtifact_default_instance_);
}
inline ::flyteidl::admin::FlyteArtifact* FlyteArtifactGetRequest::release_artifact() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.FlyteArtifactGetRequest.artifact)
  
  ::flyteidl::admin::FlyteArtifact* temp = artifact_;
  artifact_ = nullptr;
  return temp;
}
inline ::flyteidl::admin::FlyteArtifact* FlyteArtifactGetRequest::mutable_artifact() {
  
  if (artifact_ == nullptr) {
    auto* p = CreateMaybeMessage<::flyteidl::admin::FlyteArtifact>(GetArenaNoVirtual());
    artifact_ = p;
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.FlyteArtifactGetRequest.artifact)
  return artifact_;
}
inline void FlyteArtifactGetRequest::set_allocated_artifact(::flyteidl::admin::FlyteArtifact* artifact) {
  ::google::protobuf::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete reinterpret_cast< ::google::protobuf::MessageLite*>(artifact_);
  }
  if (artifact) {
    ::google::protobuf::Arena* submessage_arena = nullptr;
    if (message_arena != submessage_arena) {
      artifact = ::google::protobuf::internal::GetOwnedMessage(
          message_arena, artifact, submessage_arena);
    }
    
  } else {
    
  }
  artifact_ = artifact;
  // @@protoc_insertion_point(field_set_allocated:flyteidl.admin.FlyteArtifactGetRequest.artifact)
}

// -------------------------------------------------------------------

// DataResponse

// .flyteidl.core.LiteralMap literal_map = 1;
inline bool DataResponse::has_literal_map() const {
  return data_case() == kLiteralMap;
}
inline void DataResponse::set_has_literal_map() {
  _oneof_case_[0] = kLiteralMap;
}
inline ::flyteidl::core::LiteralMap* DataResponse::release_literal_map() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.DataResponse.literal_map)
  if (has_literal_map()) {
    clear_has_data();
      ::flyteidl::core::LiteralMap* temp = data_.literal_map_;
    data_.literal_map_ = nullptr;
    return temp;
  } else {
    return nullptr;
  }
}
inline const ::flyteidl::core::LiteralMap& DataResponse::literal_map() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.DataResponse.literal_map)
  return has_literal_map()
      ? *data_.literal_map_
      : *reinterpret_cast< ::flyteidl::core::LiteralMap*>(&::flyteidl::core::_LiteralMap_default_instance_);
}
inline ::flyteidl::core::LiteralMap* DataResponse::mutable_literal_map() {
  if (!has_literal_map()) {
    clear_data();
    set_has_literal_map();
    data_.literal_map_ = CreateMaybeMessage< ::flyteidl::core::LiteralMap >(
        GetArenaNoVirtual());
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.DataResponse.literal_map)
  return data_.literal_map_;
}

// bytes flyte_deck = 2;
inline bool DataResponse::has_flyte_deck() const {
  return data_case() == kFlyteDeck;
}
inline void DataResponse::set_has_flyte_deck() {
  _oneof_case_[0] = kFlyteDeck;
}
inline void DataResponse::clear_flyte_deck() {
  if (has_flyte_deck()) {
    data_.flyte_deck_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    clear_has_data();
  }
}
inline const ::std::string& DataResponse::flyte_deck() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.DataResponse.flyte_deck)
  if (has_flyte_deck()) {
    return data_.flyte_deck_.GetNoArena();
  }
  return *&::google::protobuf::internal::GetEmptyStringAlreadyInited();
}
inline void DataResponse::set_flyte_deck(const ::std::string& value) {
  // @@protoc_insertion_point(field_set:flyteidl.admin.DataResponse.flyte_deck)
  if (!has_flyte_deck()) {
    clear_data();
    set_has_flyte_deck();
    data_.flyte_deck_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  data_.flyte_deck_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:flyteidl.admin.DataResponse.flyte_deck)
}
#if LANG_CXX11
inline void DataResponse::set_flyte_deck(::std::string&& value) {
  // @@protoc_insertion_point(field_set:flyteidl.admin.DataResponse.flyte_deck)
  if (!has_flyte_deck()) {
    clear_data();
    set_has_flyte_deck();
    data_.flyte_deck_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  data_.flyte_deck_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:flyteidl.admin.DataResponse.flyte_deck)
}
#endif
inline void DataResponse::set_flyte_deck(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  if (!has_flyte_deck()) {
    clear_data();
    set_has_flyte_deck();
    data_.flyte_deck_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  data_.flyte_deck_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(value));
  // @@protoc_insertion_point(field_set_char:flyteidl.admin.DataResponse.flyte_deck)
}
inline void DataResponse::set_flyte_deck(const void* value, size_t size) {
  if (!has_flyte_deck()) {
    clear_data();
    set_has_flyte_deck();
    data_.flyte_deck_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  data_.flyte_deck_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(
      reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:flyteidl.admin.DataResponse.flyte_deck)
}
inline ::std::string* DataResponse::mutable_flyte_deck() {
  if (!has_flyte_deck()) {
    clear_data();
    set_has_flyte_deck();
    data_.flyte_deck_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.DataResponse.flyte_deck)
  return data_.flyte_deck_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* DataResponse::release_flyte_deck() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.DataResponse.flyte_deck)
  if (has_flyte_deck()) {
    clear_has_data();
    return data_.flyte_deck_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  } else {
    return nullptr;
  }
}
inline void DataResponse::set_allocated_flyte_deck(::std::string* flyte_deck) {
  if (has_data()) {
    clear_data();
  }
  if (flyte_deck != nullptr) {
    set_has_flyte_deck();
    data_.flyte_deck_.UnsafeSetDefault(flyte_deck);
  }
  // @@protoc_insertion_point(field_set_allocated:flyteidl.admin.DataResponse.flyte_deck)
}

// .flyteidl.admin.DynamicWorkflowNodeMetadata dynamic_workflow = 3;
inline bool DataResponse::has_dynamic_workflow() const {
  return data_case() == kDynamicWorkflow;
}
inline void DataResponse::set_has_dynamic_workflow() {
  _oneof_case_[0] = kDynamicWorkflow;
}
inline ::flyteidl::admin::DynamicWorkflowNodeMetadata* DataResponse::release_dynamic_workflow() {
  // @@protoc_insertion_point(field_release:flyteidl.admin.DataResponse.dynamic_workflow)
  if (has_dynamic_workflow()) {
    clear_has_data();
      ::flyteidl::admin::DynamicWorkflowNodeMetadata* temp = data_.dynamic_workflow_;
    data_.dynamic_workflow_ = nullptr;
    return temp;
  } else {
    return nullptr;
  }
}
inline const ::flyteidl::admin::DynamicWorkflowNodeMetadata& DataResponse::dynamic_workflow() const {
  // @@protoc_insertion_point(field_get:flyteidl.admin.DataResponse.dynamic_workflow)
  return has_dynamic_workflow()
      ? *data_.dynamic_workflow_
      : *reinterpret_cast< ::flyteidl::admin::DynamicWorkflowNodeMetadata*>(&::flyteidl::admin::_DynamicWorkflowNodeMetadata_default_instance_);
}
inline ::flyteidl::admin::DynamicWorkflowNodeMetadata* DataResponse::mutable_dynamic_workflow() {
  if (!has_dynamic_workflow()) {
    clear_data();
    set_has_dynamic_workflow();
    data_.dynamic_workflow_ = CreateMaybeMessage< ::flyteidl::admin::DynamicWorkflowNodeMetadata >(
        GetArenaNoVirtual());
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.admin.DataResponse.dynamic_workflow)
  return data_.dynamic_workflow_;
}

inline bool DataResponse::has_data() const {
  return data_case() != DATA_NOT_SET;
}
inline void DataResponse::clear_has_data() {
  _oneof_case_[0] = DATA_NOT_SET;
}
inline DataResponse::DataCase DataResponse::data_case() const {
  return DataResponse::DataCase(_oneof_case_[0]);
}
#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace admin
}  // namespace flyteidl

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // PROTOBUF_INCLUDED_flyteidl_2fadmin_2fdata_2eproto
