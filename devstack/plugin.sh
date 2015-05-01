# plugin.sh - DevStack extras.d dispatch script for Infoblox Designate backend

# check for service enabled
if is_service_enabled designate-infoblox; then

    if [[ "$1" == "source" ]]; then
        # Initial source of lib script
        #source $TOP_DIR/lib/template
	:
    fi

    if [[ "$1" == "stack" && "$2" == "pre-install" ]]; then
        # Set up system services
        #echo_summary "Configuring system services Template"
        #install_package cowsay
	:

    elif [[ "$1" == "stack" && "$2" == "install" ]]; then
        # Perform installation of service source
        echo_summary "Installing Infoblox Designate Backend"
        sudo python setup.py install

    elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
        # Configure after the other layer 1 and 2 services have been configured
        #echo_summary "Configuring Template"
        #configure_template
	:

    elif [[ "$1" == "stack" && "$2" == "extra" ]]; then
        # Initialize and start the template service
        #echo_summary "Initializing Template"
        ##init_template
	:
    fi

    if [[ "$1" == "unstack" ]]; then
        # Shut down template services
        # no-op
        :
    fi

    if [[ "$1" == "clean" ]]; then
        # Remove state and transient data
        # Remember clean.sh first calls unstack.sh
        # no-op
        :
    fi
fi

