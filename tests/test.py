from debuglogger.src.debuglogger import Logger

logger = Logger(
    process=True,
    thread=True,
    objID=True,
    mode=Logger.mode.ALL,
    func_name=True,
    filename=True,
    line=True,
)
logger.debug("test_debug")
logger.heartbeat("test_heartbeat")
logger.notice("test_notice")
logger.info("test_info")
logger.warning("test_warning")
logger.error("test_error")
logger.fatal("test_fatal")
logger.panic("test_panic")


def test():
    logger.debug("test_debug_in_func")
    logger.heartbeat("test_heartbeat_in_func")
    logger.notice("test_notice_in_func")
    logger.info("test_info_in_func")
    logger.warning("test_warning_in_func")
    logger.error("test_error_in_func")
    logger.fatal("test_fatal_in_func")
    logger.panic("test_panic_in_func")


class Test:
    def test():
        logger.debug("test_debug_in_method")
        logger.heartbeat("test_heartbeat_in_method")
        logger.notice("test_notice_in_method")
        logger.info("test_info_in_method")
        logger.warning("test_warning_in_method")
        logger.error("test_error_in_method")
        logger.fatal("test_fatal_in_method")
        logger.panic("test_panic_in_method")


test()
Test.test()
