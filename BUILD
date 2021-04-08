cc_library(
    name = "trace_interface",
    srcs = ["trace_interface.cc"],
    hdrs = ["trace_interface.h"],
)

cc_binary(
    name = "feature_trace",
    srcs = ["feature_trace.cc",
            "feature_trace.h",
    ],
    copts = ["-std=c++14",
    ],
    deps = [":trace_interface",
            #"@coworkers_project2//:gflags",
            "@local_gflags//:gflags",
    ],
)

cc_binary(
  name = "feature_to_examples",
  srcs = ["feature_to_examples.cc",
          "feature_to_examples.h",
  ],
  copts = ["-std=c++14",],
  deps = ["@com_google_absl//absl/strings",
          "@local_gflags//:gflags",
  ],
)

cc_binary(
  name = "popt",
  srcs = ["popt.cc",
          "popt.h",
  ],
  copts = ["-std=c++14",],
  deps = ["@com_google_absl//absl/strings",
          "@local_gflags//:gflags",
  ],
)
