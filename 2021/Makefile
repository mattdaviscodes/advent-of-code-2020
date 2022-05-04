DAYS := $(sort $(dir $(wildcard day-*/)))
COMMON = common

.PHONY: all $(DAYS) $(COMMON)

all: $(DAYS) $(COMMON)

$(DAYS) $(COMMON):
	$(MAKE) --directory=$@

$(DAYS): $(COMMON)
